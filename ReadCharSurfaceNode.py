# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:37:33 2019

@author: mflattery
"""
import pandas as pd

def ReadCharSurfaceNode(f='node.dat'):
        data=pd.read_csv(f,delim_whitespace=True,skiprows=[1])
        newcols=data.columns[2:]
        data=data.dropna(axis='columns')
        data.columns=newcols
        cords=data.iloc[-1]
        X=[x for x,y in zip(cords,cords.index) if 'x' in y]
        Y=[x for x,y in zip(cords,cords.index) if 'y' in y]
        T=[x for x,y in zip(cords,cords.index) if 'T' in y]
        XY=pd.DataFrame({'x':X,'y':Y,'T':T})
        XY=XY.sort_values(by='y')
        XY=XY.reset_index(drop=True)
        return XY