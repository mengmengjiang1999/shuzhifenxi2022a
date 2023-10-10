
def f(x):
    x4 = (x*x*x*x)/16
    x3 = (x*x*x)/2
    x1 = 8*x
    return x4-x3+x1-12

x0=5
x1=f(x0)
x2=f(x1)
x3=f(x2)
x4=f(x3)

print(x1)
print(x2)
print(x3)
print(x4)