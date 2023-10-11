# Enter your code here. Read input from STDIN. Print output to STDOUT

inp = input()
inp = inp.split()
n, x = int(inp[0]), int(inp[1])
scores = []
for i in range(x):
    scores.append(list(map(float, input().split())))
for i in zip(*scores):
    print(sum(i) / len(i))
