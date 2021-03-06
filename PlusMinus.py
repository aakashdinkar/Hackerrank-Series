#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    negative, positive, zero = 0,0,0
    for item in arr:
        if item < 0:
            negative += 1
        elif item > 0:
            positive += 1
        elif item == 0:
            zero += 1

    print(positive/len(arr))
    print(negative/len(arr))
    print(zero/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
