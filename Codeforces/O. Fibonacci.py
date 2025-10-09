def fib(p):
    if p == 1:
        return 0
    elif p == 2:
        return 1
    a,b = 0,1
    for i in range(3,n+1):
        a,b = b,a+b
    return b
n = int(input())
 
print(fib(n))