#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the countingSort function below.
def countingSort(arr):
    res = {}
    for item in arr:
        if not item in res:
            res[item] = 1
        else:
            res[item] += 1
    st = ""
    for item in sorted(res.keys()):
        for i in range(res[item]):
            st += str(item) + " "
    return st

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(result)
    fptr.write('\n')

    fptr.close()
