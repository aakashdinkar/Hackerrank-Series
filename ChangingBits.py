#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'changeBits' function below.
#
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#  3. STRING_ARRAY queries
#
def convert(x, y, l):
    s = ""
    for i in range(len(x)):
        if i == (len(x) - l):
            s += y
        else:
            s += x[i]
    return s

def get_val(a, b, n):
    st = bin(int("0b" + a, 2) + int("0b" + b, 2))[2:]
    if len(st) < n:
        return '0'
    else:
        return st[len(st) - (n+1)]

def changeBits(a, b, queries):
    res = ""
    for item in queries:
        lst = item.split()
        lst_item = lst[0].split('_')
        if lst_item[0] == 'set':
            if lst_item[-1] == 'a':
                a = convert(a, lst[-1], int(lst[1])+1)
            else:
                b = convert(b, lst[-1], int(lst[1])+1)
        else:
            res += get_val(a, b, int(lst[-1]))
    print(res)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    ab_size = int(first_multiple_input[0])

    queries_size = int(first_multiple_input[1])

    a = input()

    b = input()

    queries = []

    for _ in range(queries_size):
        queries_item = input()
        queries.append(queries_item)

    changeBits(a, b, queries)
