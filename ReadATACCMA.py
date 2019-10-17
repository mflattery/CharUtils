# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:28:31 2019

@author: mflattery
"""

import pandas as pd

def ReadATACCMA(f,xshift=0,y=0):
    
    with open(f,'r') as fi:
        l=fi.readline()
    x=float(l.split()[-3])    
    CleanedData=pd.read_csv(f,skiprows=[0],names=['t','hrec','na','ruch','P','lambda','Alt'],delim_whitespace=True)    
    
    CHARBC=pd.DataFrame()
    
    CHARBC['film_coeff']=CleanedData['ruch'].apply(lambda x: x * 3.28**2/2.2)
    CHARBC['P']=CleanedData['P'].apply(lambda x: x * 101305)
    CHARBC['h_rec']=CleanedData['hrec'].apply(lambda x: x * 1055*2.2)
#    CHARBC['degree_of_turbulence']=CleanedData['lambda'].apply(lambda x: round(x/(.35-.5)-0.5/(0.35-0.5),3))
    CHARBC['degree_of_turbulence']= 0 

    CHARBC['t']=CleanedData['t'].apply(lambda x: abs(x))
    CHARBC['A']=CleanedData['Alt']
    CHARBC['x']=x*2.54/100
    CHARBC['y']=y
    return CleanedData, CHARBC