a,b,c,d,e = input().split()
a=int(a)
c=int(c)
e=int(e)

if b == '+' and a+c == e:
    print("Yes")
elif b == '-' and a-c == e:
    print("Yes")
elif b == '*' and a*c == e:
    print("Yes")
else:
    if b == '+':
        print(a+c)
    elif b == '-':
        print(a-c)
    else:
        print(a*c)
        