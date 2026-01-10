n = int(input())
sum  = 0
q = 0
while q==0:
  while n>0:
    p = n%10
    sum+=p**2
    n = n//10
  if sum>9:
    n = sum
    sum=0
  else:
    q=1
    break

if sum == 1:
  print("Yes")
else:
  print("No")
  
    
