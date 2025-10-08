t = int(input())
for _ in range(t):
    n,a,b = map(int,input().split())
    minimum = float('inf')
    for i in range(0,n):
        x,y = map(int,input().split())
        d = x+y
        if (abs(x-a)+abs(y-b))<minimum:
            minimum = abs(x-a)+abs(y-b)
            
    print(minimum)
