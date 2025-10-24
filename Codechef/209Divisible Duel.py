
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    od = 0
    ev = 0
    for i in range(x,y+1):
        if i%2==0 and i%x == 0:
            ev+=i
        elif i%2!=0 and i%x == 0:
            od+=i
    if ev>=od:
        print("YES")
    else:
        print("NO")
            
