# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())
    u = s.count('U')
    d = s.count('D')
    r = s.count('R')
    l = s.count('L')
    p = [u,d,r,l]
    if (u == d and abs(r-l)==2) or (l==r and abs(u-d)==2):
        print("YES")
    else:
        print("NO")
    