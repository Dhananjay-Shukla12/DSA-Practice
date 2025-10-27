n,m = map(int,input().split())
ans = 0
for a in range(0,n+1):
    for b in range(0,m+1):
        if (((a*a) + b) == n) and (((b*b) + a) == m):
            ans+=1

print(ans)
        
        
        