from copy import deepcopy
import numpy as np
import math

def Householder_get_v(x: list)->list:
    n = len(x)

    v = deepcopy(x)

    sgm = 0 
    for item in x:
        sgm += item*item
    sgm = math.sqrt(sgm)

    v[0] += sgm

    return v

def Householder_Hx(x: list, v: list)->list:
    x1 = np.array(x)
    v1 = np.array(v)

    a1 = np.sum(np.multiply(x1,v1))
    a2 = np.sum(np.multiply(v1,v1))

    ans = x1 - 2*(a1/a2)*v1

    return list(ans)

def Householder_matrix_step1(A: list)->list:
    A1 = np.array(A)

    line1 = deepcopy(list((A1.T)[0].T))

    print(line1)



    v = Householder_get_v(line1)
    print("v=",v)

    A_new = []

    A_new_line1 = Householder_Hx(line1, v)

    A_new.append(A_new_line1)

    n = len(A)


    for i in range(1,n):
        line = deepcopy(list((A1.T)[i].T))
        A_new.append(Householder_Hx(line, v))

    A2 = []

    for i in range(1,n):
        line = []
        for j in range(1,n):
            line.append(A_new[i][j])
        A2.append(line)

    print(np.array(A_new).T)

    print(A2)
    return A_new,A2

def mifa(A: np.ndarray):
    shape = A.shape
    print("shape=",shape)
    assert(len(shape)==2 and shape[0]==shape[1])

    n = shape[0]
    u = np.ones(n)
    lmdi = 1

    for i in range(200):
        vi = np.dot(A,u)
        lmdi = max([abs(item) for item in vi])
        # print(lmdi)
        u = vi/lmdi

    return u,lmdi

A = np.array([
    [8,1,6],
    [3,5,7],
    [4,9,2]])
A_inv = np.linalg.inv(A)
print(A_inv)

u,lmd = mifa(A)
print("===mifa===")
print(u)
print(lmd)



A = [
    [1,3,4],
    [3,1,2],
    [4,2,1],
]

n = len(A)

x = [2,1,2]

v = Householder_get_v(x)

print(Householder_Hx(x,v))


for i in range(n):
    print("i",i)
    A_new,A2 = Householder_matrix_step1(A)
    A = deepcopy(A2)
    

