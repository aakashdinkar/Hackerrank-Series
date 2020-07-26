#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    dic = {}
    c = 1
    for i in range(1, n+1):
        new_dic = {}
        j = 0
        while j < arr[i-1]:
            if j % k == 0 and j != 0:
                c += 1
            if c in new_dic:
                new_dic[c].append(j+1)
            else:
                new_dic[c] = [j+1]
            j += 1
        c += 1
        dic[i] = new_dic
    c = 0
    for item in dic:
        for item2 in dic[item]:
            if item2 in dic[item][item2]:
                c += 1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
