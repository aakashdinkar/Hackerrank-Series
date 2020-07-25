#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def check(a, b, i):
    c = 0
    for item in a:
        if i % item == 0:
            c += 1
    d = 0
    for item in b:
        if item % i == 0:
            d += 1
    return c == len(a) and d == len(b)

def getTotalX(a, b):
    c = 0
    if a[-1] > b[0]:
        return 0
    for i in range(a[-1], b[0]+1):
        if check(a, b, i):
            c += 1
            print(i)
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
