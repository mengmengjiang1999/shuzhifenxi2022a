
def f(x):
    return x**5 + 4* x**3 + 1

def f6(x):
    if x==1:
        return 3
    elif x==1.5:
        return 3.25
    elif x==0:
        return 3
    elif x==2:
        return 5/3

def f12(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    elif x==2:
        return 1

ans = dict()

def juncha(f,input:list):
    print(input)
    # if input in ans.keys():
    #     return ans.get(input)
    # else:
    n=len(input)
    if n>=2:
        list1 = list()
        list2 = list()
        for i in range(n-2):
            list1.append(input[i])
            list2.append(input[i])
        list1.append(input[n-1])
        list2.append(input[n-2])
        answer = (juncha(f,list1)-juncha(f,list2))/(input[n-1]-input[n-2])
        # ans[input]=answer
        return answer
    else:
        answer=f(input[0])
        # ans[input]=answer
        return answer



print(f(0))
print(f(1))
print(f(2))

# print(juncha(f,list([0,1,2,3,4,5,6])))

# print(juncha(f6,list([0,1.5])))

# print((0.221-0.375)/16)

print(juncha(f12,list([0,0,1,2])))