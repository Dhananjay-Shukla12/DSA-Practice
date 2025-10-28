t = int(input())
for _ in range(t):
    n = int(input())
    s,t = input().split()
    c = str(sorted(s))
    d = str(sorted(t))
    if c == d:
        print("YES")
    else:
        print("NO")