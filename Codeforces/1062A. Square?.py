t = int(input())
for _ in range(t):
    a,b,c,d = map(int,input().split())
    if a==b and b==c:
        if c==d:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
        
    