# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
ls = []

for i in range(n):
    x = input()
    ls.append(x)

total = Counter(ls)
l = len(total)

print(l)
print(*total.values())
