#!/usr/bin/python

def WriteBoundary(currentshape,    charbcfile= 'CHAR/Boundary/Working.sideset.1.bc',conefile='CHAR/Boundary/aero.bc'  ):
    coords=[]
    coords.append('variables = film_coeff h_rec P degree_of_turbulence')
    
    times=currentshape.t.unique()
    DFi=currentshape[currentshape['t']==times[0]].sort_values(by='x')
    xs=DFi.x.tolist()
    ys=DFi.y.tolist()
    
    coords.append(str(len(xs)))
    for i, j in zip(xs,ys):
        linei='{0:.8f}  {1:.8f}  {2:.1f}'.format(i,j,0)
        coords.append(linei)

    print('Writing AeroBC File')
    coords.append(str(len(times)))
    for t in times:
   
        coords.append(str(t))
        DFi=currentshape[currentshape['t']==t].sort_values(by='x')
        
        for i in DFi.index:
            linei='{0:.8f}  {1:.3f}  {2:.4f}  {3:.1f} '.format(DFi.loc[i].film_coeff,DFi.loc[i].h_rec,DFi.loc[i].P,DFi.loc[i].degree_of_turbulence)
            coords.append(linei)
    
    print('writing Boundary condition file:   {} '.format(charbcfile))
    with open(charbcfile,'w') as f:
        f.writelines("%s\n" % line for line in coords)
    f.close()
    
    
#    conebc=[]
#    conebc.append('variables = time film_coeff h_rec P degree_of_turbulence ')
##    BC=currentshape.loc[57]
#    time1 = currentshape.x.iloc[(currentshape.x-0.20).abs().argsort()[:1]]
#    BC=currentshape.loc[time1.index]
#
#    for t in times:
#        BCi=BC[BC.t==t]
#        linei='{0:.5f}  {1:.8f}  {2:.3f}  {3:.4f}  {4:.1f} '.format(t,BCi.film_coeff.item(),BCi.h_rec.item(),BCi.P.item(),BCi.degree_of_turbulence.item())
#        conebc.append(linei)   
#    
##    print('writing Boundary condition file 1D Cone:   {}'.format(char1Dconebcfile))
#    with open(conefile,'w') as f:
#        f.writelines("%s\n" % line for line in conebc)
#    f.close()