#!/bin/python3

import math
import os
import random
import re
import sys


def msg(n):
    lst = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "quarter",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
    "twenty one",
    "twenty two",
    "twenty three",
    "twenty four",
    "twenty five",
    "twenty six",
    "twenty seven",
    "twenty eight",
    "twenty nine",
    "half"
    ]
    if n < 30:
        return lst[n-1]
    else:
        return lst[60-n-1]

# print(msg(48))

def timeInWords(h, n):
    hr = msg(h)
    minu = msg(n)
    if n <= 30:
        if n == 0:
            return "{} o' clock".format(hr)
        elif n != 15 and n != 30:
            if n == 1:
                return "{} minute past {}".format(minu, hr)
            return "{} minutes past {}".format(minu, hr)
        else:
            return "{} past {}".format(minu, hr)
    elif n > 30 and n < 60:
        hr = msg(h+1)
        if n != 45:
            return "{} minutes to {}".format(minu, hr)
        else:
            return "{} to {}".format(minu, hr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
