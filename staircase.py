#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        pat = ""
        for j in range(n):
            if i+j >= n-1:
                pat += "#"
            else:
                pat += " "
        print(pat)

if __name__ == '__main__':
    n = int(input())

    staircase(n)