# cook your dish here
x, k, y = map(int, input().split())

p=set()
 
i = 1
 
while i<=x:
    o = k*i
    i+=1
    p.add(o)

if y in p:
    print("YES")
else:
    print("NO")