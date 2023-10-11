import numpy

coefficients = input()
coefficients_ls = list(map(float, coefficients.split()))

x = float(input())

result = numpy.polyval(coefficients_ls, x)

print(result)
