#!/bin/python3

import os
import sys


def simpleArraySum(ar):
    sum_ar = 0
    for item in ar:
        sum_ar += item
    return sum_ar
    # return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
