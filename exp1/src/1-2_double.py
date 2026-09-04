
from numpy import double


def cal():
    result: double

    result = double(0)

    for i in range(1,2197154,1):
        result = result + double(1/i)
        print(str(i)+"\t"+str(result))


rs1 = 15.403683
rs2 = 15.179888426694328
print(rs1-rs2)
