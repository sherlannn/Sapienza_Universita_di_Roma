import numpy

inp = input().split()
n = int(inp[0])
m = int(inp[1])

arr = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    arr.append(row)

arr = numpy.array(arr, dtype = float)

print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(round(numpy.std(arr, axis = None), 11))
