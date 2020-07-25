#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the pairs function below.
def pairs(k, arr):
    a = set(arr)
    b = set(x + k for x in arr)
    return len(a&b)              

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()