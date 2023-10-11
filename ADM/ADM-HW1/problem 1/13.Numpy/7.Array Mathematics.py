import numpy

inp = input().split()
n = int(inp[0])
m = int(inp[1])

a = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    a.append(row)
a = numpy.array(a)
  
b = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    b.append(row)
b = numpy.array(b)
        

print(a + b); print(a - b); print(a * b); print(a // b); print(a % b); print(a**b)
