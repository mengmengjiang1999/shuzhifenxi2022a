import imp
from pprint import pprint


from numpy import double

def newton(x: double, f, df, lmd0 = 1)->double:
    return x - lmd0*f(x)/df(x)

# x1 = 4.86441

def get_xk(xk_1,epsl):
    return 100*xk_1/(100-epsl)

def get_fk_1(xk,xk_1,dfk_1):
    return -dfk_1*(xk-xk_1)

def get_dfk_1(xk,xk_1,fk):
    return -fk/(xk-xk_1)

x0 = 6
epsl1 = -23.3449
epsl2 = -12.329

df0 = 59

epsl = [-23.3449, -12.329, -3.3185, -0.2254, -0.001]
x0 = 6
xi = [6]

x1 = get_xk(x0,epsl1)
x2 = get_xk(x1,epsl2)
print(x1)
print(x2)

for i in range(1,6,1):
    xi.append(get_xk(xi[i-1],epsl[i-1]))

# xi
print(xi)

# df
f0 = get_fk_1(x1,x0,df0)
print(f0)

df1 = 31.0721

f1 = get_fk_1(xi[2],xi[1],df1)
print("f1 =",f1)

f2 = 2.8675

x2 = xi[2]
x3 = xi[3]
x4 = xi[4]
x5 = xi[5]

df2 = get_dfk_1(x3,x2,f2)
print("df2 =",df2)

df3 = 18.1725
f3 = get_fk_1(x4,x3,df3)
print("f3 =",f3)

f4 = 0.0008
df4 = get_dfk_1(x5,x4,f4)
print("df4 =",df4)
