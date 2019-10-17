# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:15:18 2019

@author: mflattery
"""
import pandas as pd

def TecplotReader(f):
    allines=[]
    with open(f, 'r') as a:
        for line in a:
            if 'variables' in line:
                varnames=line.split(' ')
                varnames=varnames[2:]
            else:
                try:
                    linelist=line.split()
                    linelist=[float(i) for i in linelist]
                except:
                    pass
            try:
                if len(linelist)==len(varnames):
                    allines.append(linelist)
            except:
                pass
            
        AllData=pd.DataFrame(allines,columns=varnames)    
        AllData=AllData.applymap(lambda x: float(x))
        return AllData