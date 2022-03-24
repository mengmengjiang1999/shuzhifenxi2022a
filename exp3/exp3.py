
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
    x=np.zeros((n,1))
    for i in range(0,n,1):
        x[i]=b[i]
        for j in range(0,i-1,1):
            x[i]=x[i]-L[i][j]*x[j]
    return x

# 上三角阵，解方程
# U：上三角矩阵
# n：n*n的方阵
# b：方程右边
def Uxb(U,n,b):
    x=np.zeros((n,1))
    for i in range(n,0,-1):
        if(U[i-1][i-1]==0):
            break
        x[i-1]=b[i-1]
        for j in range(n,i,-1):
            x[i-1]=x[i-1]-U[i-1][j-1]*x[j-1]
        x[i-1]=x[i-1]/U[i-1][i-1]
    return x

n=6
H = np.array(Hilbert(n))
print(H)
x = np.ones((n,1))
# print(x)
b = H.dot(x)
# print(b)

L = Cholesky(H,n)
# print(L)

LT = np.transpose(L)
# print(LT)

print(np.dot(L,LT))

# print(np.dot(L,LT)==H)

y = Lxb(L,n,b)

print(y)

x = Uxb(LT,n,y)

print(x)

# 解方程

