#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sum_valley = 0
    max_valley = 0
    for item in s:
        if item == 'U':
            sum_valley += 1
        elif item == 'D':
            sum_valley -= 1
        if sum_valley == 0:
            if item == 'U':
                max_valley += 1
    return max_valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
