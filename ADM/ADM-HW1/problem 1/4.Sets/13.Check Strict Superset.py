# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split())
c, v = 0, 0

n = int(input())
for i in range(n):
    input_data = set(input().split())
    if a.issuperset(input_data):
        c += 1
    else:
        v += 1
print('False' if v != 0 else 'True')
