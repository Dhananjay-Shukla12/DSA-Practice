n = int(input())
m = int(n**0.5)+1
freq = [0]*(n+1)

for i in range(1,m):
  x = i*i
  for j in range(i+1,m):
    y = x + j*j
    if y>n:
      break
    freq[y]+=1

ans = [i for i in range(1,n+1) if freq[i]==1]
print(len(ans))
print(*ans)
    