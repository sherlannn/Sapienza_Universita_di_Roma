# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter as c

x = int(input())
s = input().split()
s_ls = list(map(int, s))
n = int(input())
    
summ = 0
available = c(s_ls)

for i in range(n):
    xx = input().split()
    size = int(xx[0])
    price = int(xx[1])
        
    if available[size] > 0:
        summ += price
        available[size] -= 1
        
print(summ)
