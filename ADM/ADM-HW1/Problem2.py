# Ehsan Mokhtari - ehsan76m@gmail.com
# Problem 2 Solutions

########################################################################

##### Birthday Cake Candles (https://www.hackerrank.com/challenges/birthday-cake-candles)

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    # Write your code here
    n=0
    maximum = max(candles)
    size = len(candles)
    for i in range(size):
        n = n+1 if candles[i]==maximum else n
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


#############################################################################

##### Number Line Jumps Kangaroo (https://www.hackerrank.com/challenges/kangaroo)


import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1 == x2 and v1 == v2:
        return "YES"
    elif (x1 > x2 and v1 >= v2) or (x2 > x1 and v2 >= v1):
        return "NO"
    elif (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


#############################################################################

##### Viral Advertising (https://www.hackerrank.com/challenges/strange-advertising)

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    # Write your code here
    cumulative = 0
    shared = 5
    day = 1
    
    while day <= n:
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
        day += 1
    
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


############################################################################

##### Recursive Digit Sum (https://www.hackerrank.com/challenges/recursive-digit-sum)

import math
import os
import random
import re
import sys

def superDigit(n, k):
    # Write your code here
    res = str(sum(int(i) for i in n)* k) 
    
    while True:
        res = str(sum(int(i) for i in res))
        if (len(res) == 1):
            break    
    return res                

   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


##########################################################################

##### Insertion Sort - Part 1 (https://www.hackerrank.com/challenges/insertionsort1)

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    # Write your code here
    e = arr[n - 1]
    i = n - 2

    while i >= 0 and arr[i] > e:
        arr[i + 1] = arr[i]
        i -= 1
        print(*arr)

    arr[i + 1] = e
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

##################################################################################

##### Insertion Sort - Part 2 (https://www.hackerrank.com/challenges/insertionsort2)

import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

###################################################################################