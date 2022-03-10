
from cv2 import ROTATE_90_COUNTERCLOCKWISE
from numpy import double, float32


def cal():
    result: float32

    result = float32(0)

    for i in range(1,10000000,1):
        result_2 = result + float32(1/i)
        print(str(i)+"\t"+str(result))
        if result_2 == result:
            print(i)
            print("equal")
            break
        result = result_2

n = 2197152
result_n = 15.403683

result_n_1 = 15.403682

print(float32(1/n))

epsl = 0.6e-7

print(float32(epsl*result_n_1/2))