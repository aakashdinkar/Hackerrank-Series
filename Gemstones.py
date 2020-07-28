#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
    res = []
    for item in arr:
        for char in item:
            res.append(char)
    res = set(res)
    dic = {}
    for item in res:
        for word in arr:
            if item in word:
                if not item in dic:
                    dic[item] = 1
                else:
                    dic[item] += 1
    c = 0
    for item in dic:
        if dic[item] == len(arr):
            c += 1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
