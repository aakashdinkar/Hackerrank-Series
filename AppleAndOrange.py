#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_list = []
    for item in apples:
        apple_list.append(a+item)
    orange_list =[]
    for item in oranges:
        orange_list.append(b+item)
    count_apple, count_orange = 0, 0
    for item in apple_list:
        if s <= item <= t:
            count_apple += 1
    
    for item in orange_list:
        if s <= item <= t:
            count_orange += 1
    
    print(count_apple)
    print(count_orange)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
A