from numpy import double

def f1(x: double)->double:
    return x*x*x - 2*x + 2

def f2(x: double)->double:
    return -x*x*x + 5*x

def df1(x: double)->double:
    return 3*x*x - 2

def df2(x: double)->double:
    return -3*x*x + 5

def newton(x: double, f, df, lmd0 = 1)->double:
    return x - lmd0*f(x)/df(x)

def cal_newton(x0, f, df):
    #  (1) 设定合适的迭代判停准则;
    epsl1 = 1e-16
    epsl2 = 1e-10

    #  第一次迭代
    i = 0
    x1 = x0
    x2 = newton(x1, f, df)

    #  (3) 打印每个迭代步的近似解及值;
    while(abs(x2-x1)>epsl1 or abs(f(x2))>epsl2):
        # 打印结果
        i = i + 1
        print("x"+str(i)+" = "+str(x2))
        # 计算
        x1 = x2
        x2 = newton(x1, f, df)

    #  (4) 请用其他方法 (如 fzero 函数) 验证结果正确性。
    # 最终总结哪个问题需要用牛顿下山法求解，及采用牛顿下山法后的效果
    print("ans: ")
    print(x2)

    print("fzero = ")
    print(f(x2))


def cal_newton_down(x0, f, df):
    #  (1) 设定合适的迭代判停准则;
    epsl1 = 1e-10
    epsl2 = 1e-10

    #  第一次迭代
    k = 0
    x1 = x0
    x2 = x0

    #  (3) 打印每个迭代步的近似解及值;
    while(abs(x2-x1)>epsl1 or abs(f(x2))>epsl2):
        # 计算
        x1 = x2
        x2 = newton(x1, f, df)

        #  (2) 设置合适的下山因子序列;
        lmd0 = 0.9
        i = 0

        # 下山
        while(abs(f(x2))>=abs(f(x1))):
            print("lambda"+str(i)+" = "+str(lmd0))
            if i<10:
                x2 = newton(x1, f, df, lmd0)
            else:
                break
            lmd0 = lmd0/2
            i = i + 1

        print("x"+str(k)+" = "+str(x2))


    #  (4) 请用其他方法 (如 fzero 函数) 验证结果正确性。
    # 最终总结哪个问题需要用牛顿下山法求解，及采用牛顿下山法后的效果
    print("ans: ")
    print(x2)

    print("fzero = ")
    print(f(x2))

# 对第一题求解
# cal_newton(0, f1, df1)
cal_newton_down(0, f1, df1)

# 对第二题求解
# cal_newton(1.35, f2, df2)
# cal_newton_down(1.35, f2, df2)