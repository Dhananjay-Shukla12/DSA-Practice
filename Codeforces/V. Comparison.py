a, b, c = input().split()
a = int(a)
c = int(c)
 
if b == '=' and a == c:
    print("Right")
elif b == '>' and a > c:
    print("Right")
elif b == '<' and a < c:
    print("Right")
else:
    print("Wrong")
