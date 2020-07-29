#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    dic = {}
    for item in contests:
        if not item[1] in dic:
            dic[item[1]] = [item[0]]
        else:
            dic[item[1]].append(item[0])
    luck = 0
    if 1 in dic:
        luck += sum(sorted(dic[1], reverse = True)[:k])
        luck -= sum(sorted(dic[1], reverse = True)[k:])
    if 0 in dic:
        luck += sum(dic[0])
    return luck

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
