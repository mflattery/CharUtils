#!/usr/bin/python
import pandas as pd

def ReadATAC(f,xshift=0):
    allines=[]
    with open(f, 'r') as a:
        for line in a:
            if 'VARIABLES' in line:
                varnames=line.split('"')[1:-1]
                varnames=[var for var in varnames if ',' not in var]
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
        
        CharBC=pd.DataFrame(columns=['x','y','film_coeff','P','h_rec','t','degree_of_turbulence'])
        for time in AllData['time'].unique():
            TimeStep=AllData[AllData['time']==time]
            AllDataGrouped=TimeStep.groupby('Z (ft)').max()
            AllDataGroupedAvg=TimeStep.groupby('Z (ft)').mean()
            AllDataGrouped=AllDataGrouped.reset_index()
            AllDataGroupedAvg=AllDataGroupedAvg.reset_index()
    
            CleanedData=pd.DataFrame()
            CleanedData['x']= AllDataGrouped['Z (ft)'].apply(lambda x: x /3.28 + xshift)
            CleanedData['y']=AllDataGrouped['Y (ft)'].apply(lambda x: x /3.28)
            CleanedData['film_coeff']=AllDataGrouped['ruch (lbm/ft2-sec)'].apply(lambda x: x * 3.28**2/2.2)
            CleanedData['P']=AllDataGrouped['p (atm)'].apply(lambda x: x * 101305)
            CleanedData['h_rec']=AllDataGrouped['recov enth (BTU/lbm)'].apply(lambda x: x * 1055*2.2)
            CleanedData['t']=AllDataGrouped['time']
            CleanedData['degree_of_turbulence']=AllDataGrouped['laminar/turb']
            CharBC=CharBC.append(CleanedData)
            
        return AllData, CharBC