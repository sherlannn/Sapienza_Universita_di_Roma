from collections import deque

d = deque()

cmds = ['append', 'pop', 'popleft', 'appendleft']

n = int(input())
for _ in range(n):
    x = input().split()
    cmd = x[0]
    if cmd == cmds[0]:
        d.append(int(x[1]))
    elif cmd == cmds[1]:
        d.pop()
    elif cmd == cmds[2]:
        d.popleft()
    elif cmd == cmds[3]:
        d.appendleft(int(x[1]))

print(*d)
