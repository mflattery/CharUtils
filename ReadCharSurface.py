#!/usr/bin/python
import pandas as pd

def ReadCharSurface(f='CHAR//out.tec.boundary.final'):
    currentshape=pd.read_csv(f,delim_whitespace=True,skiprows=4,names=['x','y','z','T','2','3','4','5','6'])
    currentshape=currentshape.dropna()  
    currentshape=currentshape.sort_values(by='y')
    currentshape=currentshape.reset_index(drop=True)
    return currentshape