from numpy import double 


def get_xk(xk_1,epsl):
    return 100*xk_1/(100-epsl)

def get_fxrk(xlk,xrk,xuk,fxlk):
    return -1*(xuk-xrk)*fxlk/(xuk-xlk)

def get_epsl(xk,xk_1):
    return 100*(xk-xk_1)/xk

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

xr3 = 1.84819
xr4 = 1.8639

epsl3 = get_epsl(xr3,xr2)
epsl4 = get_epsl(xr4,xr2)

print(epsl3,epsl4)