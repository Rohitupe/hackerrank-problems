#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a,b):
    alice_count = 0
    bob_count = 0
    for i in range(len(a) and len(b)):
        if a[i] > b[i]:
            alice_count += 1
        if a[i] < b[i]:
            bob_count +=1
        else:
            None
    return alice_count,bob_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
