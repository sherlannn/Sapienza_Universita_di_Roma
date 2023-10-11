import numpy as np



n = int(input())
arr1 = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    arr1.append(row)

arr1 = np.array(arr1)

arr2 = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr2.append(row)

arr2 = np.array(arr2)

print(np.dot(arr1, arr2))
