#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    arr_dic = {}
    brr_dic = {}
    for item in arr:
        if not item in arr_dic:
            arr_dic[item] = 1
        else:
            arr_dic[item] += 1
    for item in brr:
        if not item in brr_dic:
            brr_dic[item] = 1
        else:
            brr_dic[item] += 1    
    res = []
    # print(arr_dic, brr_dic)
    for item in arr_dic:
        if item in brr_dic and arr_dic[item] != brr_dic[item]:
            if not item in res:
                res.append(item)
        elif not item in brr_dic:
            if not item in res:
                res.append(item)
    for item in brr_dic:
        if item in arr_dic and arr_dic[item] != brr_dic[item]:
            if not item in res:
                res.append(item)
        elif not item in arr_dic:
            if not item in res:
                res.append(item)
    return sorted(res)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
