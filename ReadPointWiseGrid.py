#!/usr/bin/python

import pandas as pd

def ReadPointWiseGrid(GridFile='NoseTipGrid.dat'):
    coords=[]
    with open(GridFile,'r') as f:
        for line in f.readlines():
            linelist=line.split()
            if len(linelist)>1:
                L=[float(li) for li in linelist][0:2]
                coords.append(L)
    
    XY=pd.DataFrame(coords)
    XY.columns=['x','y']
    XY=XY.drop_duplicates().reset_index(drop=True)
    XY=XY.sort_values(by='x').reset_index(drop=True)
    return XY

if __name__=='__main__':
    ReadPointWiseGrid(GridFile='../Grid/NoseNew.dat')