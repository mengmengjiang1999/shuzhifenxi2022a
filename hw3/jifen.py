import math



def f4(x):
    return math.sqrt(1+x)

def f6(x):
    return math.exp(-x*x)

def f121(x):
    return x*x*math.exp(-x)

def f122(x):
    return 2*x/(x*x-4)

def simpson(func,a,b):
    ba = b-a
    ab = a+b
    return ba*(func(a)+4*func(ab/2)+func(b))/6

def simpson38(func,a,b):
    ba=b-a
    h=ba/3
    return h*(func(a)+3*func(a+h)+3*func(b-h)+func(b))*3/8

def tixing(func,a,b):
    return (func(a)+func(b))*(b-a)/2

def tixingN(func,a,b,N):
    h=(b-a)/N
    ans = 0
    for k in range(0,N):
        ans += tixing(func,a+k*h,a+(k+1)*h)
    return ans

def simpsonN(func,a,b,N):
    h=(b-a)/N
    ans = 0
    for k in range(0,N):
        ans += simpson(func,a+k*h,a+(k+1)*h)
    return ans



# print(simpson(f4,0,0.1))
# print(simpson38(f4,0,0.1))
# print(tixingN(f6,0.2,1.5,4))
# print(tixingN(f6,0.2,1.5,8))
# print(simpsonN(f6,0.2,1.5,2))
# print(simpsonN(f6,0.2,1.5,4))
a=1
b=1.6
t10 = tixing(f122,a,b)
print("t10",tixing(f122,a,b))
t11 = tixingN(f122,a,b,2)
print("t11",tixingN(f122,a,b,2))
t20 = (4*t11-t10)/(4-1)
print("t20",t20)
t12 = tixingN(f122,a,b,4)
t21 = (4*t12-t11)/(4-1)
t30 = (4*4*t21-t20)/(4*4-1)
print("t12",t12)
print("t21",t21)
print("t30",t30)
