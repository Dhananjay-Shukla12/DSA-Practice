t = int(input())
for _ in range(t):
    n = int(input())
    if n<3:
        n=4
    elif n%3==0:
        n=(n//3)*5
    elif n%3==1:
        n=((n//3)-1)*5+8
    else:
        n=(n//3)*5+4
    
    print(n)
    
        