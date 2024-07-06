#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n): 
    for row in range(n):
        for s in range(n-row-1):
            print(end=' ')
        for a in range(row+1):
            print('#', end='')
        print()

if __name__ == '__main__':
    n = int(input())

    staircase(n)
