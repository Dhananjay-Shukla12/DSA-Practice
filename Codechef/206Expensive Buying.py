
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    i = 0
    arr = sorted(arr,reverse = True)
    sum = 0
    while i<k:
        sum = sum + arr[i]
        i+=1
    print(sum)
        
        