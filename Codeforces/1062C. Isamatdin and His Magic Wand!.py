t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    od = 0
    ev = 0
    for i in arr:
        if i%2==0:
            ev+=1
        else:
            od+=1
    
    if od!=0 and ev!=0:
        arr.sort()
    
    print(*arr)