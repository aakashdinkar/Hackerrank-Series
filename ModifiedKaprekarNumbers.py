#!/bin/python3

import math
import os
import random
import re
import sys

def split(s):
    l = 10 ** len(str(s))
    return (s*s) % l, int((s*s)/l)

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    res = []
    for i in range(p, q+1):
        a, b = split(i)
        # print(a, b)
        if (a + b) == i:
            res.append(str(i))
    if len(res) > 0:
        print(" ".join(res))
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
