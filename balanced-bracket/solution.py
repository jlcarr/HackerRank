#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    close_map = {c[0]:c[1] for c in ['()', '{}', '[]']}
    stack = []
    for c in s:
        if c in close_map:
            stack.append(close_map[c])
        elif stack and c == stack[-1]:
            stack.pop()
        else:
            return "NO"
    if stack:
        return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

