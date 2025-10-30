t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    sum = 0
    k = 0
    for i in range(1,n+1):
        if i>x:
            sum+=i
            k+=1
    
    profit = sum - (x*k)
    print(profit)
            
    