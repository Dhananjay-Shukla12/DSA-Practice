n = int(input())
if n==0:
    print(0,0,0)
elif n==1:
    print(1,0,0)
elif n==2:
    print(1,1,0)
else:
    a=0
    b=1
    k=0
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
        if n//c == 3:
            k=1
            print(c,c,c)
            break
        elif (a+b+c) == n:
            k=1
            print(a,b,c)
            break

    if k==0:
        print("I'm too stupid to solve this problem")