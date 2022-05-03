# Jacobi

from cmath import e
from copy import deepcopy
import numpy as np

def maxitem(x0:np.ndarray, x1:np.ndarray):
    max = 0
    for i in range(len(x0)):
        # print(i)
        # print(abs(x0[i]-x1[i]))
        if max < abs(x0[i][0]-x1[i][0]):
            max = abs(x0[i][0]-x1[i][0])
    return max

def sqrt_item(x0: np.ndarray, x1:np.ndarray):
    sum = 0
    for i in range(len(x0)):
        sum += abs(x0[i][0]-x1[i][0])*abs(x0[i][0]-x1[i][0])
    return sum

'''
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
'''

def jacobi(n:int, A: np.ndarray, b: np.ndarray):
    
    x0 = np.zeros((n,1),dtype=np.double)

    assert(len(A.shape)==2)
    assert(len(b.shape)==2)
    assert(A.shape[0]==A.shape[1]==n)
    assert(b.shape[1]==1)
    assert(b.shape[0]==n)

    line = 1e-3
    cnt = 0

    x1 = deepcopy(b)
    for i in range(n):
        x1[i][0] = x1[i][0]/A[i][i]

    delta = maxitem(x0,x1)

    # print("new" + str(cnt))
    # print(x1)

    while delta>line:
        # print("delta")
        # print(delta)

        cnt += 1
        x0 = deepcopy(x1)

        for i in range(n):
            sumi = 0
            for j in range(i):
                sumi += A[i][j]*x0[j][0]
            for j in range(i+1,n):
                sumi += A[i][j]*x0[j][0]
            x1[i][0] = (1/A[i][i])*(b[i]-sumi)

        # print("new" + str(cnt))
        # print(x1)
        # print(-0.2*(2*x0[1]+x0[2])-2.4)
        # print(-0.25*(-x0[0]+2*x0[2])+5)
        # print(-0.1*(2*x0[0]-3*x0[1])+0.3)
        # # print(x0)
        delta = maxitem(x0,x1)
        # delta = maxitem(x0,x1)
        # print("delta="+str(delta))

    # print("x1")
    # print(x1)
    # # return x1
    # print(5*x1[0]+2*x1[1]+x1[2])
    # print(-x1[0]+4*x1[1]+2*x1[2])
    # print(2*x1[0]-3*x1[1]+10*x1[2])
    return x1

# Jacobi迭代法，特殊类型矩阵
def jacobi_for_4(n:int, A: np.ndarray, b: np.ndarray):
    
    x0 = np.zeros((n,1),dtype=np.double)

    assert(len(A.shape)==2)
    assert(len(b.shape)==2)
    assert(A.shape[0]==A.shape[1]==n)
    assert(b.shape[1]==1)
    assert(b.shape[0]==n)

    line = 1e-3
    cnt = 0

    x1 = deepcopy(b)
    for i in range(n):
        x1[i][0] = x1[i][0]/A[i][i]

    delta = maxitem(x0,x1)

    # print("new" + str(cnt))
    # print(x1)

    while delta>line:
        # print("delta")
        # print(delta)

        cnt += 1
        x0 = deepcopy(x1)

        for i in range(0,n):
            sumi = 0
            if i-1>=0:
                sumi += A[i][i-1]*x0[i-1][0]
            if i+1<n:
                sumi += A[i][i+1]*x0[i+1][0]
            x1[i][0] = (b[i]/A[i][i])-sumi/A[i][i]

        # print("new" + str(cnt))
        # print(x1)
        # # print(x0)
        delta = maxitem(x0,x1)
        # delta = maxitem(x0,x1)
        # print("delta="+str(delta))
    print("Jacob迭代次数", cnt)
    return x1

# Gauss-Seidel迭代法，特殊类型矩阵
def gs_for_4(n:int, A: np.ndarray, b: np.ndarray):
    
    x0 = np.zeros((n,1),dtype=np.double)

    assert(len(A.shape)==2)
    assert(len(b.shape)==2)
    assert(A.shape[0]==A.shape[1]==n)
    assert(b.shape[1]==1)
    assert(b.shape[0]==n)

    line = 1e-3
    cnt = 0

    x1 = deepcopy(x0)
    x1[0][0] = 1

    delta = maxitem(x0,x1)

    while delta>line:
        # print("delta")
        # print(delta)

        cnt += 1
        x1 = deepcopy(x0)
        # x0 = deepcopy(x1)

        for i in range(0,n):
            sumi = 0
            if i-1>=0:
                sumi += A[i][i-1]*x0[i-1][0]
            if i+1<n:
                sumi += A[i][i+1]*x0[i+1][0]
            x0[i][0] = (b[i]/A[i][i])-sumi/A[i][i]

        # print("new" + str(cnt))
        # print(x0)
        # # print(x0)
        delta = maxitem(x0,x1)
        # print("delta",delta)
        
    print("GS迭代次数", cnt)
    return x1


# SOR迭代法，特殊类型矩阵
def SOR_for_4(n:int, A: np.ndarray, b: np.ndarray, omg: np.double):
    
    x0 = np.zeros((n,1),dtype=np.double)

    assert(len(A.shape)==2)
    assert(len(b.shape)==2)
    assert(A.shape[0]==A.shape[1]==n)
    assert(b.shape[1]==1)
    assert(b.shape[0]==n)

    line = 1e-3
    cnt = 0

    x1 = deepcopy(x0)
    x1[0][0] = 1

    delta = maxitem(x0,x1)

    while delta>line:
        # print("delta")
        # print(delta)

        cnt += 1
        x1 = deepcopy(x0)
        # x0 = deepcopy(x1)

        for i in range(0,n):
            sumi = 0
            if i-1>=0:
                sumi += A[i][i-1]*x0[i-1][0]
            if i+1<n:
                sumi += A[i][i+1]*x0[i+1][0]
            x0[i][0] = (1-omg)*x0[i][0] + omg * (b[i]/A[i][i])-sumi/A[i][i]

        # print("new" + str(cnt))
        # print(x0)
        # # print(x0)
        delta = maxitem(x0,x1)
        # print("delta",delta)
        
    print("SOR 迭代次数", cnt)
    return x1


def y(x:np.double, a:np.double, epsl:np.double)->np.double:
    return ((1-a)*(1-pow(e,-x/epsl))/(1-pow(e,-1/epsl)))+ a*x

epsl = 0.0001
a = 1/2
n = 100
h=1/n
size = n-1
A = np.zeros((size,size),dtype=np.double)
for i in range(size):
    if i-1>=0:
        A[i][i-1]=epsl
    A[i][i]=-(2*epsl+h)
    if i+1<size:
        A[i][i+1]=epsl+h

b = np.zeros((size,1),dtype=np.double)
for i in range(size):
    b[i][0] = a*h*h
b[size-1][0] -= epsl
b[size-1][0] -= h

A2 = np.array([
    [5,2,1],
    [-1,4,2],
    [2,-3,10]
],dtype=np.double)
b2 = np.array([
    [-12],
    [20],
    [3]
],dtype=np.double)
n2 = 3
# ans = jacobi(n2, A2, b2)
# print(np.dot(A2,ans))

print("epsl =",epsl)

print("A")
print(A)

print("\nb")
print(b)

print("精确解")
ansy = np.array([[y(i*h,a,epsl) for i in range(1,n)]]).reshape(1,-1).T
print(ansy)

ans = jacobi_for_4(size, A, b)
ans_b = np.dot(A,ans)

ans2 = gs_for_4(size, A, b)
ans_b_2 = np.dot(A,ans2)

ans3 = SOR_for_4(size, A, b, 1.05)
ans_b_3 = np.dot(A,ans3)

print("Jacob answer")
print(ans)
print("A*ans_jacob")
print(ans_b)
print("Jacob迭代法误差")
print(maxitem(b,ans_b))
ans_max_3 = maxitem(ans3,ansy)
print("Jacob和精确解之间误差")
print(ans_max_3)

print("Gauss Seidel answer")
print(ans2)
print("A*ans_gs")
print(ans_b_2)
print("GS迭代法误差")
print(maxitem(b,ans_b_2))
ans_max_3 = maxitem(ans3,ansy)
print("GS和精确解之间误差")
print(ans_max_3)

print("SOR answer")
print(ans3)
print("A*ans_sor")
print(ans_b_3)
print("SOR迭代法误差")
print(maxitem(b,ans_b_3))
print("SOR和精确解之间误差")
ans_max_3 = maxitem(ans3,ansy)
print(ans_max_3)

'''
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
'''