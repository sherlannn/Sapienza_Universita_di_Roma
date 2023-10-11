import numpy

inp = input().split()
n = int(inp[0])
m = int(inp[1])

array = []
for i in range(n):
    inp = input().split()
    row = list(map(int, inp))
    array.append(row)

array = numpy.array(array)

print(array.T)
print(array.flatten())
