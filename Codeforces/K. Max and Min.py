a,b,c = map(int,input().split())
maximum = None
minimum = None
if a>=b and a>=c:
    maximum = a
elif b>=c and b>=a:
    maximum = b
else:
    maximum = c
    
if a<=b and a<=c:
    minimum = a
elif b<=c and b<=a:
    minimum = b
else:
    minimum = c
    
print(minimum,maximum)
