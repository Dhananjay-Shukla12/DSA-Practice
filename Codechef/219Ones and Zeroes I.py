t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())
    one = 0
    zero = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '0':
            zero+=1
        else:
            one+=1
        
        if one>=zero:
            ans+=1
    
    print(ans)
        