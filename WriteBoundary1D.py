
#!/usr/bin/python
def WriteBoundary1D(currentshape, Length,  conefile='CHAR/Boundary/aero.bc' ):
    
    times=currentshape.t.unique()
    conebc=[]
    conebc.append('variables = time film_coeff h_rec P degree_of_turbulence ')
    time1 = currentshape.x.iloc[(currentshape.x-Length).abs().argsort()[:1]]
    BCid=currentshape.loc[time1.index]
    BC=currentshape[currentshape.x==BCid.x.item()]
    for t in times:
        BCi=BC[BC.t==t]
        linei='{0:.5f}  {1:.8f}  {2:.3f}  {3:.4f}  {4:.1f} '.format(t,BCi.film_coeff.item(),BCi.h_rec.item(),BCi.P.item(),BCi.degree_of_turbulence.item())
        conebc.append(linei)   
    
#    print('writing Boundary condition file 1D Cone:   {}'.format(char1Dconebcfile))
    with open(conefile,'w') as f:
        f.writelines("%s\n" % line for line in conebc)
    f.close()
    
    return BC

def WriteBoundary1DCMA(currentshape,  conefile='CHAR/Boundary/aero.bc'  ):
    times=currentshape.t.unique()
    conebc=[]
    conebc.append('variables = time film_coeff h_rec P degree_of_turbulence ')
    BC=currentshape

    for t in times:
        BCi=BC[BC.t==t]
        linei='{0:.5f}  {1:.8f}  {2:.3f}  {3:.4f}  {4:.1f} '.format(t,BCi.film_coeff.item(),BCi.h_rec.item(),BCi.P.item(),BCi.degree_of_turbulence.item())
        conebc.append(linei)   
    
#    print('writing Boundary condition file 1D Cone:   {}'.format(char1Dconebcfile))
    with open(conefile,'w') as f:
        f.writelines("%s\n" % line for line in conebc)
    f.close()
    
    return BC