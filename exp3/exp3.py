
from copy import deepcopy
import numpy as np


# 生成Hilbert矩阵
def Hilbert(n:int):
    H = []
    for i in range(1,n+1,1):
        hi=[]
        for j in range(1,n+1,1):
            hi.append(1/(i+j-1))
        H.append(hi)
    return H

# 巧克力分解
# 分成下三角巧克力和上三角巧克力
# def Cholesky(A):
#     L=A
#     n = np.shape(A)[0]
#     # 先求第一列
#     L[0][0]=np.sqrt(A[0][0])
#     for i in range(1,n,1):
#         L[i][0]=L[i][0]/L[0][0]
#     # 求第2到n列
#     for j in range(1,n,1):
#         # 求对角线上的元素
#         arr = L[j][0:j]
#         ajj= np.vdot(arr,arr)
#         L[j][j]=np.sqrt(A[j][j]-ajj)
#         # 求剩余元素
#         for i in range(j,n,1):
#             li = L[i][0:j-1]
#             lj = L[j][0:j-1]
#             L[i][j] = (A[i][j]-np.vdot(li,lj))/L[j][j]
#     return L

# Cholesky分解，已进行测试
def Cholesky(A,n):
    L=A
    for j in range(1,n+1,1):
        for k in range(1,j,1):
            L[j-1][j-1] = L[j-1][j-1]-L[j-1][k-1]*L[j-1][k-1]
        L[j-1][j-1]=np.sqrt(L[j-1][j-1])
        for i in range(j+1,n+1,1):
            for k in range(1,j,1):
                L[i-1][j-1]=L[i-1][j-1]-L[i-1][k-1]*L[j-1][k-1]
            L[i-1][j-1]=L[i-1][j-1]/L[j-1][j-1]
    for i in range(0,n):
        for j in range(i+1,n):
            L[i][j]=0
    return L

# 下三角阵，解方程
# L：下三角矩阵
# n：n*n的方阵
# b：方程右边
def Lxb(L,n,b):
    print("Lxb")
    print(L)
    print("b")
    print(b)
    x=np.zeros((n,1))
    for i in range(0,n,1):
        print("x")
        print(x)
        x[i]=b[i]
        for j in range(0,i,1):
            x[i]=x[i]-L[i][j]*x[j]
        x[i]=x[i]/L[i][i]
    print("Lxb ans")
    print(x)
    return x

# 上三角阵，解方程
# U：上三角矩阵
# n：n*n的方阵
# b：方程右边
def Uxb(U,n,b):
    print("Uxb")
    print(U)
    print("b")
    print(b)
    x=np.zeros((n,1))
    for i in range(n-1,-1,-1):
        print("x")
        print(x)
        if(U[i][i]==0):
            break
        x[i]=b[i]
        for j in range(n-1,i,-1):
            x[i]=x[i]-U[i][j]*x[j]
        x[i]=x[i]/U[i][i]
    return x

n=2
H = np.array(Hilbert(n))
print("Hilbert")
print(H)

Hbt = deepcopy(H)
print(Hbt)

x = np.ones((n,1))
# print(x)
b = H.dot(x)
print("b =",b)

L = Cholesky(H,n)
print("\nL")
print(L)

LT = np.transpose(L)
print("\nLT")
print(LT)

print("\nnp.dot(L,LT)")
print(np.dot(L,LT))

# print(np.dot(L,LT)==H)

y = Lxb(L,n,b)
print("y =",y)

x = Uxb(LT,n,y)
print("x =",x)

# 解方程

