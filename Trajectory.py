#!/usr/bin/python
import math
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import RK45

def Traj(V,  Gamma,  DragFile='DragCoefficientI3.xlsx', Mrv=181.8,  A=math.pi*(11.82*2.54/100)**2,hi=399000/3.28):
    
    Me=5.9736e24
    ge=6.67e-11
    
    G=ge*Me
    
    re=6.371e6
    ho=hi+re
    Vx=V*math.cos(math.radians(Gamma))
    Vy=V*math.sin(math.radians(Gamma))
    Vz=0
    y0=np.array([0,ho,0,Vx,Vy,Vz])

    CDdata=pd.read_excel(DragFile)
    CDf=interp1d(CDdata['A'],CDdata['CD'])

    def T(h):
        if h>=25000:
            T=-131.21+0.00299*h
        elif 11000<=h<25000:
            T=-56.46
        elif h<11000:
            T=15.04-0.00649*h
        return T
    
    def P(h,T=T):
        if h>=25000:
            P=2.488*((T(h)+273.1)/216.6)**(-11.388)
        elif 11000<=h<25000:
            P=22.65*math.exp(1.73-0.000157*h)
        elif h<11000:
            P=101.29*((T(h)+273.1)/288.08)**5.256
        return P
    
    def rho(h,P=P,T=T):
        r=P(h)/(.2869*(T(h)+273.1))
        return r

    def dvy(t,y,G=G):
    
        r=y[0:3]
        v=y[3:6]
        
        rnorm=np.linalg.norm(r)
        rhat=r/rnorm
        
        vnorm=np.linalg.norm(v)
        vhat=v/vnorm
        den=rho(y[1]-re)
        cd=CDf(y[1]-re)
        
        fun= -  0.5*den*cd*vnorm**2*vhat*A/Mrv   -   G/rnorm**2*rhat
        
        dy=np.concatenate((v,fun))
        return dy
    
    RK=RK45(dvy,0,y0,120,max_step=0.1)
    
    a=ho
    Y=RK.y
    time=[RK.t]
    while a>100:
        try:
            RK.step()
            Y=np.vstack((Y,RK.y))
            time.append(RK.t)
            a=RK.y[1]-re
        except:
            a=10
        
    Result=pd.DataFrame(Y)
    Result.columns=['x','y','z','Vx','Vy','Vz']
    Result=Result.drop(['z','Vz'],axis=1)
    Result['t']=time
    Result['A']=Result['y']-re
    Vel=[]
    
    for i in range(len(Result['t'])):
        vi=np.sqrt(Result.loc[i,'Vx']**2+Result.loc[i,'Vy']**2)        
        Vel.append(vi)
        
    Result['V']=Vel
    
    return Result