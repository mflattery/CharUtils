
import jinja2

def GenerateATACFile(Trajectory,XY,tstart,tend,xshift=0,
                     Tw=530.0,Temp='ATAC/RVTemplate2.inp',
                     ATACinp='ATAC/ATAC.inp',rn=1.4,deg=8.2,Endx=68,Endy=11.012,Tfinal=39,dt1=0.1):

    with open(Temp,'r') as tmp:
        ATACtemplate=jinja2.Template(tmp.read())
        
    TrajectLines=''
    for i in range(0,len(Trajectory)):
        Dfi=Trajectory.loc[i]
        linei=' {0:.4f}  {1:>6.1f}  {2:>5.1f}  0  0  0  1 \n'.format(Dfi.t,Dfi.A,Dfi.V)
        TrajectLines=TrajectLines+linei
    
    FinalTraj=Trajectory.loc[len(Trajectory)-1]
    linei='-{0:.4f}  {1:>6.1f}  {2:>5.1f}  0  0  0  1 '.format(FinalTraj.t,FinalTraj.A,FinalTraj.V)
    TrajectLines=TrajectLines+linei  
        
    GridLines=''
#    XY=XY[XY['x']<0.13]
    XY['y']=XY['y'].apply(lambda x: x*3.28*12)
    XY['x']=XY['x'].apply(lambda x: (x-xshift)*3.28*12)
    rmax=len(XY)-3
    for i in range(0,rmax,3):
        
        GridLines+='  3  4  0  0 \n'            
        cord='   {0:.8f}  {1:.8f}  {2:.8f}  {3:.8f}  {4:.8f}  {5:.8f}  {6:.8f}  {7:.8f} \n'.format(
                XY.loc[i].x,XY.loc[i].y,XY.loc[i+1].x,XY.loc[i+1].y,XY.loc[i+2].x,XY.loc[i+2].y,XY.loc[i+3].x,XY.loc[i+3].y)
        GridLines+= cord
        GridLines+='  1  2  1  0  0  0  0  0 \n'  
    
    End=XY.loc[len(XY)-1]    
    GridLines+=' -1  4  0  0 \n'
    cord='   {0:.8f}  {1:.8f}  {2:.8f}  {3:.8f} \n'.format(
                End.x,End.y,Endx,Endy)
    GridLines+= cord
    GridLines+='  1  2  1  0  0  0 '   
    WallTemp='{:.1f}'.format(Tw)
    Tbegin='{:.4f}'.format(tstart)
    Tend='{:.4f}'.format(tend)
    dt='{:.4f}'.format(dt1)
    with open(ATACinp,'w') as f:
        f.write(ATACtemplate.render(tinit=Tbegin,
                                    tfinal=Tend,
                                    Trajectory=TrajectLines,
                                    rn=rn,
                                    deg=deg,
                                    Tw=WallTemp,
                                    dt1=dt,
                                    coordinates=GridLines,Tend=Tfinal
                ))
    f.close()
    
if __name__=='__main__':
    GenerateATACFile()