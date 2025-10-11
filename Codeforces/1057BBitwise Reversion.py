t = int(input())
for _ in range(t):
    x,y,z = map(int,input().split())
    ans = 0
    for i in range(31):
        xb = (x>>i) & 1
        yb = (y>>i) & 1
        zb = (z>>i) & 1
        
        if (xb,yb,zb) not in [(0,0,0), (0,1,0), (0,0,1), (1,0,0), (1,1,1)]:
            ans = 1
            break
    if ans == 1:
        print("NO")
    else:
        print("YES")
        