# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = str(input())
    b = str(input())
    a_count = a.count('1')
    b_count = b.count('1')
    if a_count%2 == b_count%2:
        print("YES")
    else:
        print("NO")