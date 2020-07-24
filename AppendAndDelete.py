#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    i, c = 0, 0
    while c < min(len(s), len(t)) and s[c] == t[c]:
        c += 1
    if k % 2 == (len(s) + len(t)) % 2:
        i = len(s) + len(t) - 2*c
    else:
        i = len(s) + len(t) + 1
    if k < i:
        return 'No'
    return 'Yes'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
