t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    disleft = 50-x
    mini = 2*y
    maximum = 2*y+10
    if disleft>=mini and disleft<=maximum:
        print("Yes")
    else:
        print("No")
    