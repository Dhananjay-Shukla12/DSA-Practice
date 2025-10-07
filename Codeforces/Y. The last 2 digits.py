a,b,c,d = map(int,input().split())
 
ans = str(a*b*c*d)
n=len(ans)
print(ans[n-2]+ans[n-1])
