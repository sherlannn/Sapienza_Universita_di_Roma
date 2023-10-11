import numpy

arr = input().split()
arr = list(map(int, arr))
arr = numpy.array(arr)
res = arr.reshape(3, 3)
print(res)
