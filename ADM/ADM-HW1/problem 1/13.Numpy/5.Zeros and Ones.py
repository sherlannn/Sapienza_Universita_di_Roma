import numpy

inp = input()
inp = inp.split()
d = [int(x) for x in inp]

print(numpy.zeros(tuple(d), dtype=int))
print(numpy.ones(tuple(d), dtype=int))

