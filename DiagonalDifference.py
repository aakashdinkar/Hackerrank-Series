#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sum_first_diagonal = 0
    sum_second_diagonal = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                sum_first_diagonal += arr[i][j]
            if i+j+1 == len(arr):
                sum_second_diagonal += arr[i][j]
    return abs(sum_first_diagonal - sum_second_diagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
