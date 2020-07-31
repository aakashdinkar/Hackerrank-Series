#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    string = "hackerrank"
    ind = 0
    if len(string) > len(s):
        return "NO"
    for i in range(len(s)):
        if ind < len(string) and s[i] == string[ind]:
            ind += 1
    if ind == len(string):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
