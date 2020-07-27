#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    c = 0
    for i in range(0, len(s), 3):
        if s[i:i+3] != 'SOS':
            if s[i] != 'S':
                c += 1
            if s[i+1] != 'O':
                c += 1
            if s[i+2] != 'S':
                c += 1
            # c += 1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
