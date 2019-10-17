# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:11:01 2019

@author: mflattery
"""

import pandas as pd
import matplotlib.pyplot as plt

alllines=[]
with open('../ASCCBC/case10.out') as fil:
    lines=fil.readlines()
    
    for i in range(len(lines)):
        if 'BODY POINT LOCATION AND SURFACE ENERGY BALANCE RESULTS' in lines[i]:
            
            sliceline=lines[i-2].split()
            datalines=[]
            for j in range(i+8,i+28):
                linei=lines[j].split()
                for k in range(len(linei)):
                    if '*' in linei[k]:
                        new=linei[k].split('*')[0]
                        linei[k]=new
                linei.extend([sliceline[2],sliceline[6]])
                linefloat=[float(u) for u in linei]
                alllines.append(linefloat)

AsccData=pd.DataFrame(alllines,columns=['ptnum','x_in','y_in','T_R','Sdot','Sdote',"B",'Emdot','ruch','Hrsp','P','A','t'])

pt15=AsccData[AsccData.ptnum==15]
pt16=AsccData[AsccData.ptnum==16]
pt17=AsccData[AsccData.ptnum==17]

plt.plot(pt15.A,pt15.ruch.apply(lambda x: x*3.28**2/2.2),'.-')
plt.plot(pt16.A,pt16.ruch.apply(lambda x: x*3.28**2/2.2),'.-')
plt.plot(pt17.A,pt17.ruch.apply(lambda x: x*3.28**2/2.2),'.-')

plt.legend(('20','22','24'))

