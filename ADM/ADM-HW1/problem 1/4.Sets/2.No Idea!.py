# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input().split()
m = input().split()
a = set(input().split())
b = set(input().split())

count = 0

for value in m:
    count = count + 1 if value in a else count - 1 if value in b else count


print(count)
