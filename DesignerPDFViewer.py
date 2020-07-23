#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    lst = []
    for i in word:
        lst.append(h[ord(i) - 97])
    max_value = max(lst)
    return len(word) * max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
