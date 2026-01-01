# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    if n==2:
        print(-1)
    else:
        for i in range(n):
            for j in range(n):
                if i == 0:
                    print(1, end=" ")
                elif j == n-1:
                    print(1, end=" ")
                elif j == n-2 and i<=2:
                    print(1, end=" ")
                else:
                    print(0, end=" ")
            print("")