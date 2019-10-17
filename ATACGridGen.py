#!/usr/bin/python

import pandas as pd

def ReadInitialSurface(GridFile='NoseTipGrid.dat'):#Grid=pd.read_csv('NoseTipGrid.dat',skiprows=[0])
    coords=[]
    with open(GridFile,'r') as f:
        for line in f.readlines():
            linelist=line.split()
            if len(linelist)>1:
                L=[float(li) for li in linelist][0:2]
                coords.append(L)
    
    XY=pd.DataFrame(coords)
    XY.columns=['x','y']
    XY=XY.sort_values(by='x').reset_index(drop=True)
    return XY
    
#    GridLines=[]
#    for i in range(0,len(XY)-4,4):
#        GridLines.append('  3  4  0  0')
#        cord='   {0:.4f}  {1:.4f}  {2:.4f}  {3:.4f}  {4:.4f}  {5:.4f}  {6:.4f}  {7:.4f}'.format(
#                XY.loc[i].x,XY.loc[i].y,XY.loc[i+1].x,XY.loc[i+1].y,XY.loc[i+2].x,XY.loc[i+2].y,XY.loc[i+3].x,XY.loc[i+3].y)
#        GridLines.append(cord)
#        GridLines.append('  1  2  1  0  0  0  0  0')
#    
#    charbcfile= 'ATACGrid.dat'  
#    with open(charbcfile,'w') as f:
#        f.writelines("%s\n" % line for line in GridLines)
#    f.close()
        