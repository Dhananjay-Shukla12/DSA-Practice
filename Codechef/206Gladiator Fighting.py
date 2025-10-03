
t = int(input())
for _ in range(t):
    n = int(input())
    
    minimum = n-2
    maximum = (minimum * (minimum+1))//2
    print(minimum," ",maximum)

