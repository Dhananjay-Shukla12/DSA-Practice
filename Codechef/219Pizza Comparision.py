# cook your dish here
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    
    if n/100 == m/225:
        print("Equal")
    elif n/100 < m/225:
        print("Small")
    else:
        print("Large")