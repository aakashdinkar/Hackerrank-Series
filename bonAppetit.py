#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    sum_bill = 0
    c = 0
    for i in range(len(bill)):
        if i != k:
            c += 1
            sum_bill += bill[i]  
    if (sum_bill/2) == b:
        print("Bon Appetit")
    else:
        print(int(bill[k]/2))


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
