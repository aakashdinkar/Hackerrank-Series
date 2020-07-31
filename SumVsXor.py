#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sumXor function below.
def sumXor(n):
    if n == 0:
        return 1
    c = bin(n)[2:]
    return 2 ** c.count('0')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
