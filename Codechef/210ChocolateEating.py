t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    sum = 0
    if a == b:
        sum = (a+b)-1
    else:
        sum = a+b
    print(sum)
        