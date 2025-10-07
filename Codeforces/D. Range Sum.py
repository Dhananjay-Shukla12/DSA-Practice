t = int(input())
for _ in range(t):
    sum = 0
    n,m = map(int,input().split())
    piku = n
    samy = m
    n = n*(n+1)//2
    m = m*(m+1)//2
    ans = abs(m - n)
    if piku>samy:
        ans+=samy
    elif piku<samy:
        ans+=piku
    print(ans)