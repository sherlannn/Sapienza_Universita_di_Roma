import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    res = numpy.array(arr[::-1], float)
    return res

arr = input().strip().split(' ')
result = arrays(arr)
print(result)