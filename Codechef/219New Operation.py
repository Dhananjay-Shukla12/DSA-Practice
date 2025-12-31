# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    low = 0
    high = 0
    k = list(reversed(arr))
    for i in range(n-1):
        arr[i] = arr[i+1]*2 + arr[i]
        low = arr[i]
        arr[i+1] = low
    
    for i in range(1,n):
        k[i] = k[i-1]*2 + k[i]
        high = k[i]
        k[i-1] = high
    
    print(low,high)