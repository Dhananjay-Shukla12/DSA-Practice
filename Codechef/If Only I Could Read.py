T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    j=0
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            j=i
            break
        else:
            j=-1
    
    if j==-1:
        print(-1)
    else:
        print(j+1,j+2)
            