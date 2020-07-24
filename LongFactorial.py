#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    print(num)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
