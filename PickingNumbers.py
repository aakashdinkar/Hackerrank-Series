#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()
    max_val = -1
    i = n - 1
    while i >= 0:
        count = 0
        j = i - 1
        while j >= 0:
            if abs(a[i] - a[j]) <= 1:
                count += 1
            j -= 1
        if count > max_val:
            max_val = count
        i -= 1
    return max_val+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
