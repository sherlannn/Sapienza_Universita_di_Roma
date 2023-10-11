import numpy
numpy.set_printoptions(legacy='1.13')

inp = input().split()
n = int(inp[0])
m = int(inp[1])
print(numpy.eye(n, m,dtype=float))
