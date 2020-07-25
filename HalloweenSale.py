#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    lst = []
    c = 0
    if p > s:
        return 0
    for i in range(p, m, -d):
        if i >= m and sum(lst) <= s:
            lst.append(i)
            c += 1
    
    c1 = (s - sum(lst)) // m
    return c + c1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
