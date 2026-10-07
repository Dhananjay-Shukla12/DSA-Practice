# cook your dish here
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    s = str(input())
    l = str(input())
    
    left = set()
    right = set()
    for i in l:
        left.add(i)
    for i in s:
        if i not in left:
            right.add(i)
    
    left_a = 0
    right_a = 0
    ans = 0
    for i in s:
        if i in left:
            if right_a>ans:
                ans = right_a
            right_a = 0
            left_a+=1
        elif i in right:
            if left_a>ans:
                ans = left_a
            left_a = 0
            right_a +=1
    if right_a>ans:
        ans = right_a
    if left_a>ans:
        ans = left_a
    print(ans)
            
            