#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    val = [0] * 1001
    for i in arr:
        val[i] += 1
    counter = 0
    val = val[::-1]
    ans = []
    for i in val:
        if i > 0:
            counter += i
            ans.append(counter)
    ans = ans[::-1]
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
