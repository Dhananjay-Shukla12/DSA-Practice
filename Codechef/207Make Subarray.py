t = int(input())

for i in range(t):
    n = int(input())
    s = str(input())
    yo = -1
    wai = -1
    for i in range(0,n):
        if s[i] == '1' and yo==-1:
            yo = i
        if s[i] == '1' and i!=yo:
            wai = i
    ans = 0
    for i in range(yo,wai):
        if s[i]=='0':
            ans+=1
    print(ans)
                
            
    