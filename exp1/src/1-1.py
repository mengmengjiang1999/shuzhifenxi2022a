from cProfile import label
from cmath import sin
from operator import itemgetter

from numpy import double, real, log10

def trunc(h: double, M: double)->double:
    return M*h/2

def round(h: double, epsl: double)->double:
    return 2*epsl/h


def f_trunc(h)->double:
    return trunc(h, 1)

def f_round(h)->double:
    return round(h, 1e-16)

def f_sum(h)->double:
    return f_trunc(h)+f_round(h)

import matplotlib.pyplot as plt

# x = [pow(10,i) for i in range(-16,1,1)]

x : list[double]
x = []
iii = 1
for i in range(0,-17,-1):
    print("ttt")
    x.append(iii)
    print(x)
    iii = iii/10
x.reverse()

print(x)

y : list[double]
trn: list[double]
rnd: list[double]

y = [f_sum(item) for item in x]
trn = [f_trunc(item) for item in x]
rnd = [f_round(item) for item in x]

print(y)
print(trn)
print(rnd)


plt.axes(xscale = "log")  
# plt.axes(yscale = "log")  

plt.xlabel("step h")
plt.ylabel("error(log)")

# plt.plot(x, y, label="sum")
# plt.plot(x, trn, label="truncation")
# plt.plot(x, rnd, label="rounding")

plt.plot(x, [log10(item) for item in y], label="sum")
plt.plot(x, [log10(item) for item in trn], label="truncation")
plt.plot(x, [log10(item) for item in rnd], label="rounding")

plt.legend()
plt.show()