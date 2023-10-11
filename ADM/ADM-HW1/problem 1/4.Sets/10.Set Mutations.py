n = int(input())
s = set(map(int, input().split()))
num_cmds = int(input())

for _ in range(num_cmds):
    cmd, *args = input().split()
    get_set = set(map(int, input().split()))
    if cmd == 'intersection_update':
        s.intersection_update(get_set)
    elif cmd == 'update':
        s.update(get_set)
    elif cmd == 'difference_update':
        s.difference_update(get_set)
    elif cmd == 'symmetric_difference_update':
        s.symmetric_difference_update(get_set)

print(sum(s))
