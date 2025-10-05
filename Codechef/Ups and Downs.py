t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    for i in range(1,len(arr)-1,2):
        swp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = swp
    print(*arr)
    