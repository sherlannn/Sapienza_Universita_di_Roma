from collections import deque

num = int(input())
for i in range(num):
    inp1 = input()
    inp2 = input().split()
    inp2 = deque(map(int, inp2))
    
    flag = 1
    l = len(inp2)
    

    for j in range(l- 1):
        if inp2[0] >= inp2[1]:
            inp2.popleft()
        elif inp2[-1] >= inp2[-2]:
            inp2.pop()
        else:
            flag = 0
            break

    if flag ==1:
        print("Yes")
    else:
        print("No")
