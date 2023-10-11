import numpy

inp = input().split()
n = int(inp[0])
m = int(inp[1])

arr = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    arr.append(row)

arr = numpy.array(arr)
print(numpy.prod(numpy.sum(arr, axis=0)))
