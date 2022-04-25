from numpy import double 


def get_xk(xk_1,epsl):
    return 100*xk_1/(100-epsl)

def get_fxrk(xlk,xrk,xuk,fxlk):
    return -1*(xuk-xrk)*fxlk/(xuk-xlk)

xl1 = 1
xr1 = 1.42
xu1 = 2
fxl1 = -0.5634
xr1 = 1.42
epsl2 = 19.2207
xr2 = get_xk(xr1,epsl2)
print("xr2 =",xr2)

fxr1 = get_fxrk(xl1,xr1,xu1,fxl1)
print("fxr1 =",fxr1)