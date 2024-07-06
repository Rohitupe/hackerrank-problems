#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length_arr = len(arr)
    negative_count = 0
    positive_count = 0
    zeros_count = 0
    for i in arr:
        if i==0:
            zeros_count += 1
        if i < 0:
            negative_count += 1
        if i > 0:
            positive_count += 1
    positive = round(positive_count/length_arr,6)
    negative = round(negative_count/length_arr,6)
    zeros = round(zeros_count/length_arr,6)
    print(f"{positive}\n{negative}\n{zeros}")
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
