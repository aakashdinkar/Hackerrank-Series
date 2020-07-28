#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    p = arr[0]
    left = []
    right = []
    equal = []
    for item in arr:
        if item == p:
            equal.append(item)
        elif item < p:
            left.append(item)
        else:
            right.append(item)
    res = []
    for item in left:
        res.append(item)
    for item in equal:
        res.append(item)
    for item in right:
        res.append(item)
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
