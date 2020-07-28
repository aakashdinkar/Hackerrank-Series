#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    res = []
    for item in s:
        res.append(ord(item))
    s_res = []
    for i in range(len(res)-1):
        s_res.append(abs(res[i] - res[i+1]))
    res.reverse()
    r_res = []
    for i in range(len(res)-1):
        r_res.append(abs(res[i] - res[i+1]))
    if r_res == s_res:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
