# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
a = set(map(int, input().strip().split(' ')))
m = int(input())
b = set(map(int, input().strip().split(' ')))
    
print(len(a.symmetric_difference(b)))
