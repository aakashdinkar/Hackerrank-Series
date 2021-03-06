#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the countingSort function below.
def countingSort(arr, n):
    s = Counter(arr)
    return (s[i] for i in range(100))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr, n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
