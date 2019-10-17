# -*- coding: utf-8 -*-
"""
Created on Mon May 13 19:15:37 2019

@author: mflattery
"""
import pandas as pd
import numpy as np
def ReadAsccCase(f,xshift=0,y=0.05,BLT=70000):
    alllines=[]
    visclines=[]
    with open(f) as fil:
        lines=fil.readlines()
        
        for i in range(len(lines)):
            if 'BODY POINT LOCATION AND SURFACE ENERGY BALANCE RESULTS' in lines[i]:
                
                sliceline=lines[i-2].split()
                for j in range(i+8,i+48):
                    linei=lines[j].split()
                    for k in range(len(linei)):
                        if '*' in linei[k]:
                            new=linei[k].split('*')[0]
                            linei[k]=new
                    linei.extend([sliceline[2],sliceline[6]])
                    linefloat=[float(u) for u in linei]
                    alllines.append(linefloat)
#            if 'VISCOUS FLOW - WALL AND B. L. RECOVERY PROPERTIES' in lines[i]:
#                
#                sliceline=lines[i-2].split()
#                for j in range(i+8,i+48):
#                    linei=lines[j].split()
#                    for k in range(len(linei)):
#                        if '*' in linei[k]:
#                            new=linei[k].split('*')[0]
#                            linei[k]=new
#                    linei.extend([sliceline[2],sliceline[6]])
#                    linefloat=[float(u) for u in linei]
#                    visclines.append(linefloat)
    
    AsccData=pd.DataFrame(alllines,columns=['ptnum','x_in','y_in','T_R','Sdot','Sdote',"B",'Emdot','ruch','Hrsp','P','A','t'])
#    AsccData2=pd.DataFrame(visclines,columns=['ptnum','integ','s','T_w','Hw','wrho',"wvisc",'hrec','rec','Q','CF','A','t'])    
#    AsccData=AsccData.merge(AsccData2,how='inner',on=['ptnum','A','t'])
    
    ruchun=[]
    for i, row in AsccData.iterrows():
        
        if row.A>BLT:
            un=(2*.5*row.B)/(np.exp(2*.5*row.B)-1)
        else:
            un=(2*.35*row.B)/(np.exp(2*.35*row.B)-1)
#        print(row)
        ruchun.append(row.ruch/un)
        
    AsccData['ruchUN']=ruchun

    CharBC=pd.DataFrame(columns=['x','y','film_coeff','P','h_rec','t','degree_of_turbulence'])
    for time in AsccData['t'].unique():
        AllDataGrouped=AsccData[AsccData['t']==time]
#        AllDataGrouped=TimeStep.groupby('Z (ft)').max()
#        AllDataGroupedAvg=TimeStep.groupby('Z (ft)').mean()
#        AllDataGrouped=AllDataGrouped.reset_index()
#        AllDataGroupedAvg=AllDataGroupedAvg.reset_index()

        CleanedData=pd.DataFrame()
        CleanedData['x']= AllDataGrouped['x_in'].apply(lambda x: x *2.54/100 + xshift)
        CleanedData['y']=AllDataGrouped['y_in'].apply(lambda x: x *2.54/100)
#        CleanedData['y']=y
        CleanedData['film_coeff']=AllDataGrouped['ruchUN'].apply(lambda x: x * 3.28**2/2.2)
        CleanedData['P']=AllDataGrouped['P'].apply(lambda x: x * 101305)
        CleanedData['h_rec']=AllDataGrouped['Hrsp'].apply(lambda x: x * 1055*2.2)
        CleanedData['t']=AllDataGrouped['t']
        if AllDataGrouped.A.max()>BLT:
            CleanedData['degree_of_turbulence']= 0
        else :
            CleanedData['degree_of_turbulence']= 1

        CleanedData['A']=AllDataGrouped['A']
        
        CharBC=CharBC.append(CleanedData)
            
    return AsccData, CharBC
    