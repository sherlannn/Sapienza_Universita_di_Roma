import numpy

n = int(input())

arr = []
for _ in range(n):
    inp = input()
    inp = [float(x) for x in inp.split()]
    arr.append(inp)

arr = numpy.array(arr, dtype=float)
print(round(numpy.linalg.det(arr), 2))
