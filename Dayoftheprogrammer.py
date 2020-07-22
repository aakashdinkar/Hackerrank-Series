#!/bin/python3

import math
import os
import random
import re
import sys
import calendar

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    feb = 28
    if year == 1918:
        return "{}.09.{}".format(41-15, year)
    elif year < 1918:
        if year % 4 == 0:
           feb += 1
    else:
        if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
            feb += 1
    return "{}.{}.{}".format(41-feb,'09',year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
