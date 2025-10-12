a,b,c,d,e = map(int,input().split())
k = {}
piku = [a,b,c,d,e]
for i in piku:
  if i in k:
        k[i] += 1
  else:
        k[i] = 1
p=0
q=0
for key,value in k.items():
  if value == 3:
    p=1
  if value == 2:
    q=1
if p==1 and q==1:
  print("Yes")
else:
  print("No")
  
  