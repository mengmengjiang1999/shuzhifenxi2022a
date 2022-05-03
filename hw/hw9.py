from copy import deepcopy
import numpy as np

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

def fanmifa(A_inv: np.ndarray):
    shape = A_inv.shape
    print("shape=",shape)
    assert(len(shape)==2 and shape[0]==shape[1])

    n = shape[0]
    u = np.ones(n)
    lmdi = 1

    for i in range(300):
        vi = np.dot(A_inv,u)
        lmdi = 1/max([abs(item) for item in vi])
        # print(lmdi)
        u = vi*lmdi

    return u,lmdi

def Householder_get_v(alpha: np.ndarray):
    assert(len(alpha.shape)==2)
    assert(alpha.shape[1]==1)
    # 假设alpha是一个列向量

    # v
    sgm = np.sign(alpha[0][0])*np.linalg.norm(alpha)
    v = deepcopy(alpha)
    v[0][0] += sgm

    # 计算Ha
    return v

def Householder_step(alpha: np.ndarray, x:np.ndarray):
    print(alpha)

    print(alpha.shape)

    assert(len(alpha.shape)==2)
    assert(alpha.shape[1]==1)

    assert(alpha.shape==x.shape)
    # 假设alpha是一个列向量

    # v
    # sgm = np.sign(alpha[0][0])*np.linalg.norm(alpha)
    # v = deepcopy(alpha)
    # v[0][0] += sgm

    v = Householder_get_v(alpha)

    # 计算Ha
    return x-2*(np.dot(v.T,x)/(np.dot(v.T,v)))*v

def Householder_matrix(A:np.ndarray):
    assert(len(A.shape)==2)
    
    n = A.shape[1]

    AT = A.T

    for i in range(n):
        ha = Householder_step(AT[0].reshape(1,-1), AT[i].reshape(1,-1))
        print(ha)

A = np.array([
    [7,3,-2],
    [3,4,-1],
    [-2,-1,3]])
A_inv = np.linalg.inv(A)
print(A_inv)

u,lmd = mifa(A)
print("===mifa===")
print(u)
print(lmd)

u_min,lmd_min = fanmifa(A_inv)
print("===fanmifa===")
print(u_min)
print(lmd_min)

A2 = np.array([
    [6,2,1],
    [2,3,1],
    [1,1,1]
])
I = np.array([
    [1,0,0],
    [0,1,0],
    [0,0,1]
])
A2_inv = np.linalg.inv(A2-2*I)
u_min,lmd_min = fanmifa(A2_inv)
print("===fanmifa===")
print(u_min)
print(lmd_min)


A_8 = np.array([
    [4,0,0],
    [4,5,5],
    [2,5,5],
])
Householder_matrix(A_8)