# 利用 2. 6. 3 节给出的 fzerotx 程序，在 MATLAB 中编程求第一类的零阶贝塞尔函数J0(x)的零点. 
# J0(x)在MATLAB 中通过 besselj(0,x) 得到. 
# 试求J0(x)的前10个正的零点, 并绘出函数曲线和零点的位置

# 参考资料：http://dong.sh/posts/pybessel/


from scipy.special import jv
from re import L
from numpy import double
from numpy import sign

import numpy as np
import matplotlib.pyplot as plt

def draw_bessel():
    x = np.arange(0, 100, 0.1)

    plt.figure(figsize=[10,5])
    y0 = jv(0,x)
    y1 = jv(1,x)
    y2 = jv(2,x)
    y3 = jv(3,x)

    plt.rcParams['font.family'] = 'Times New Roman'
    plt.plot(x, y0, label='order 0')
    # plt.plot(x, y1, label='order 1')
    # plt.plot(x, y2, label='order 2',c='b')
    # plt.plot(x, y3, label='order 3') 

    # ab = [i for i in range(40)]
    # ans = [jv(0,item) for item in ab]

    # print(ans)

    plt.legend()
    plt.show()

def func(x):
    return jv(0,x)


ab_query = [(2,3),(5,6),(8,9),(11,12),(14,15),(18,19),(21,22),(24,25),(27,28),(30,31)]

def zeroin(func, s: double, t:double)->double:
    a = s
    b = t
    fa = func(a)
    fb = func(b)
    if fa==0:
        return fa
    if fb==0:
        return fb
    if sign(fa)==sign(fb):
        print("fa*fb>0")
        return -1
    c = a
    fc = fa
    d = b-c
    e=d

    epsl1 = 1e-16

    while(abs(fb)>epsl1):
        if sign(fa)==sign(fb):
            a = c
            fa = fc
            d = b-c
            e=d
        if abs(fa)<abs(fb):
            c=b
            b=a
            a=c
            fc=fb
            fb=fa
            fa=fc
        m = 0.5*(a-b)
        eps_float = 0.6e-7 # float accuracy
        eps_double = 1e-16
        tol = 2.0 * eps_double * max(abs(b), 1.0)
        if abs(m)<=tol or fb==0.0:
            break
        if abs(e)<tol or abs(fc)<=abs(fb):
            d=m
            e=m
        else:
            s=fb/fc
            if a==c:
                p = 2.0*m*s
                q=1.0-s
            else:
                q = fc/fa
                r = fb/fa
                p = s*(2.0*m*q*(q-r)-(b-c)*(r-1.0))
                q = (q-1.0)*(r-1.0)*(s-1.0)
            if p>0:
                q = -q
            else:
                p = -p
            if (2.0*p<3.0*m*q-abs(tol*q)) and (p<abs(0.5*e*q)):
                e=d
                d=p/q
            else:
                d=m
                e=m
        
        c=b
        fc=fb
        if abs(d)>tol:
            b = b+d
        else:
            b=b-sign(b-a)*tol
        fb = func(b)

    return b


# draw_bessel()

def run():
    ans = []
    for item in ab_query:
        print(item)
        ans.append(zeroin(func, item[0], item[1]))
    func_ans = [func(item) for item in ans]

    x = np.arange(0, 50, 0.1)    
    plt.figure(figsize=[10,5])
    y0 = jv(0,x)
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.plot(x, y0, label='bessel 0')


    print(ans)
    print(func_ans)

    # for i in ans:
    for i in range(len(ans)):
        plt.scatter(ans[i], func_ans[i], c='r')  # stroke, colour
        plt.annotate('('+str(format(ans[i], '.2f'))+',0)', xy=(ans[i],0), xytext=(ans[i],-0.1*(i%2-0.5))) 

    # plt.plot(ans, func_ans, label = 'zero')

    plt.legend()
    plt.show()

run()