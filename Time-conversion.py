#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    a = s.split(':')
    if s[-2:] == 'PM':
        if int(a[0]) != 12: 
            a = s.split(':')
            a[0] = str(int(a[0])+12)
            return ":".join(a)[:-2]
    elif s[-2:] == 'AM':
        if int(a[0]) == 12:
            a[0] = str(int(a[0])-12) + '0'
            return ":".join(a)[:-2]
    return s[:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
