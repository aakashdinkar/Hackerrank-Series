#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    sum_bar = 0
    count = 0
    for i in range(0,len(s)):
        if i + m - 1 < len(s):
            for j in range(i, i+m):
                sum_bar += s[j]
            print(sum_bar)
            if sum_bar == d:
                count += 1
            sum_bar = 0
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
