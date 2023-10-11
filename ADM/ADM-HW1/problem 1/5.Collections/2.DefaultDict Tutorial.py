# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

inp = input().split()
n = int(inp[0])
m = int(inp[1])
d = defaultdict(list)

for i in range(1, n + 1):
    s = input()
    d[s].append(str(i))

for i in range(m):
    query = input()
    result = d.get(query, ['-1'])
    print(' '.join(result) if result != ['-1'] else -1)

