import numpy
numpy.set_printoptions(legacy="1.13")

inp = input().split()

arr = numpy.array(inp,dtype=float)

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
