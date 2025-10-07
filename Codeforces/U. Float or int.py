import math
n = float(input())
if math.floor(n)==math.ceil(n):
    print("int",int(n))
else:
    print("float",math.floor(n),n-math.floor(n))