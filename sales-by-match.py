#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    empty_list = []
    var = []
    count = 0
    for i in ar:
        if i not in empty_list:
            empty_list.append(i)

    for j in empty_list:
        if ar.count(j) >= 2:
            var.append(ar.count(j))


    for l in var:
        if l % 2 ==0:
            output = l//2
            count += output
        elif l%2 != 0:
            ot = l//2
            count += ot

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
