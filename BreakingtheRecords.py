#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_value, min_value, count_max, count_min = scores[0], scores[0], 0 , 0
    for i in range(1,len(scores)):
        if scores[i] < min_value:
            min_value = scores[i]
            count_min += 1
        elif scores[i] > max_value:
            max_value = scores[i]
            count_max += 1
    return [count_max, count_min]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
