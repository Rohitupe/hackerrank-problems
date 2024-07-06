#!/bin/python3

import os
import sys
import datetime

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    newDate = datetime.datetime.strptime(s,'%I:%M:%S%p')
    odate = datetime.datetime.strftime(newDate,'%H:%M:%S')
    return odate
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
