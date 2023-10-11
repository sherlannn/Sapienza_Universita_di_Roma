#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    t1_out = datetime.datetime.strptime(t1, format)
    t2_out = datetime.datetime.strptime(t2, format)
    delta = t1_out - t2_out
    return delta
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        delta = delta.total_seconds()
        if delta<0:
            delta = delta * (-1)    
        delta = int(delta)
        fptr.write(str(delta) + '\n')

    fptr.close()
