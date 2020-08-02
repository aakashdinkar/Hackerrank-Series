#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    lst = sorted(list(set(scores)), reverse = True)
    res = []
    l = len(lst)
    for item in alice:
        while (l > 0) and (item >= lst[l - 1]):
            l -=1
        res.append(l+1)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
