import math
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    nuone = arr.count(1)
    ntwo = arr.count(2)
    nthree = arr.count(3)
    
    # for i in range(0,len(arr)):
    #     if arr[i]==1:
    #         nuone+=1
    #     elif arr[i]==2:
    #         ntwo+=1
    #     else:
    #         nthree+=1
    
    sum = 0
    sum = nuone * (nuone - 1) // 2 
    sum += nuone*ntwo
    sum += ntwo*nthree
    print(sum)
    