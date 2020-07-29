#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):
    dic = {}
    i = 1
    for item in orders:
        if not sum(item) in dic:
            dic[sum(item)] = [i]
        else:
            dic[sum(item)].append(i)
        i += 1
    res = []
    for item in sorted(dic.keys()):
        for char in dic[item]:
            res.append(char)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
