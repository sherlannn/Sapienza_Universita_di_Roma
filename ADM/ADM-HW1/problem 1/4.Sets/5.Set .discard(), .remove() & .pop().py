n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    command, *args = input().split()
    getattr(s, command)(*map(int, args))

print(sum(s))
