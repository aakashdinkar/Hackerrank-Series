#!/bin/python3

import math
import os
import random
import re
import sys

def twoArrays(k, A, B):
    a = sorted(A)
    b = sorted(B, reverse = True)
    for item1, item2 in zip(a, b):
        if (item1 + item2) < k:
            return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
