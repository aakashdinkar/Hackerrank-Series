#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    lst = {}
    for i in range(len(a)):
        if a[i] in lst:
            lst[a[i]].append(i)
        else:
            lst[a[i]] = [i]
    min_val, ch = 9999, 0
    for item in lst:
        if len(lst[item]) == 2:
            a = lst[item]
            c = abs(a[0] - a[1])
            if c < min_val:
                min_val = c
    if min_val == 9999:
        return -1
    return min_val
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
