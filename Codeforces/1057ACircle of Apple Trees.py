t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    k = set()
    for _ in arr:
        k.add(_)
    print(len(k))
    