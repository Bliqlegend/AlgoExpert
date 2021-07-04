#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    acount = 0
    for i in s:
        if i=='a':
            acount+=1
    remains = n%len(s)
    if remains == 0:
        repeat = int(n/len(s))
        acount *= repeat
    else:
        repeat = int(n/len(s))
        acount *= repeat
        newS = s[:remains]
        for i in newS:
            if i=='a':
                acount+=1
    return acount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
