#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    def check(arr):
        a = sorted(arr)
        return not (a[0] + a[1]) <= a[2]
    lst = list(set(filter(check, list(combinations(sticks, 3)))))
    def add(arr):
        return sum(arr)
    res_dic = {}
    res = list(map(add, lst))
    for i, j in zip(res, lst):
        if not i in res_dic:
            res_dic[i] = [sorted(list(j))]
        else:
            res_dic[i].append(j)
    print(res_dic)
    res_max = []
    res_min = []
    if not res:
        return [[-1]]
    elif res.count(max(res)) == 1:
        return res_dic[max(res)]
    else:
        for item in res_dic[max(res)]:
            res_max.append(list(item))
            res_min.append(list(item))
        if res_max.count(max(res_max)) > 1:
            if res_min.count(max(res_min)) > 1:
                return list(res_dic[max(res)][0])
            else:
                return list(res_dic[max(res)][res_min.index(max(res))])
        else:
            return list(res_dic[max(res)][res_max.index(max(res_max))])
    # print(res_dic)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)
    
    fptr.write(' '.join(map(str, result[0])))
    fptr.write('\n')

    fptr.close()
