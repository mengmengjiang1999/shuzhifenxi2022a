# Jacobi

import numpy as np

def maxitem(x0, x1):
    max = 0
    for i in range(len(x0)):
        # print(i)
        # print(abs(x0[i]-x1[i]))
        if max < abs(x0[i]-x1[i]):
            max = abs(x0[i]-x1[i])
    return max



def jacobi():

    x0 = [0, 0, 0]
    line = 1e-2

    cnt = 0

    x1 = [-2.4, 5, 0.3]
    delta = maxitem(x0, x1)

    while delta>line:
        cnt += 1
        x0 = [item for item in x1]
        x1[0] = -0.2*(2*x0[1]+x0[2])-2.4
        x1[1] = -0.25*(-x0[0]+2*x0[2])+5
        x1[2] = -0.1*(2*x0[0]-3*x0[1])+0.3
        print("new" + str(cnt))
        print(x1)
        # print(x0)
        delta = maxitem(x0,x1)
        print("delta="+str(delta))

    print(5*x1[0]+2*x1[1]+x1[2])
    print(-x1[0]+4*x1[1]+2*x1[2])
    print(2*x1[0]-3*x1[1]+10*x1[2])


def gauss_seidel():
    line = 1e-2

    x1 = [1, 0, 0]
    x0 = [0, 0, 0]
    delta = maxitem(x0, x1)

    cnt = 0
    while delta>line:
        cnt += 1
        x1 = [item for item in x0]
        x0[0] = -0.2*(2*x0[1]+x0[2])-2.4
        x0[1] = -0.25*(-x0[0]+2*x0[2])+5
        x0[2] = -0.1*(2*x0[0]-3*x0[1])+0.3
        print("new" + str(cnt))
        print(x0)
        # print(x0)
        delta = maxitem(x0,x1)
        print("delta="+str(delta))

    print(5*x1[0]+2*x1[1]+x1[2])
    print(-x1[0]+4*x1[1]+2*x1[2])
    print(2*x1[0]-3*x1[1]+10*x1[2])


gauss_seidel()