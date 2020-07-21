#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    dic = {}
    for item in arr:
        if item not in dic:
            dic[item] = 0
        else:
            dic[item] += 1
    min_key, max_value = None, -1
    for key in dic:
        if dic[key] > max_value:
            max_value = dic[key]
            min_key = key
    return min_key

arr = list(map(int, input().rstrip().split()))
print(migratoryBirds(arr))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr_count = int(input().strip())

#     arr = Counter(map(int, input().rstrip().split()))

#     result = migratoryBirds(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()
