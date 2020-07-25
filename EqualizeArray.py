#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    max_val = -1
    for i in range(len(arr)):
        c = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                c += 1
            if c > max_val:
                max_val = c
    return n - max_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
