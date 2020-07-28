#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    st = ""
    for item in s:
        if item.isalpha():
            print(ord(item)+k)
            if item.isupper():
                a = 'A'
                st += chr(ord(a) + (ord(item) - ord(a) + k) % 26)
            else:
                a = 'a'
                st += chr(ord(a) + (ord(item) - ord(a) + k) % 26)
        else:
            st += item
    return st

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
