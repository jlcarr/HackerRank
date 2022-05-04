#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def print_arr(arr):
    print(' '.join(map(str,arr)))

def insertionSort1(n, arr):
    index = n-1
    v = arr[index]
    index -= 1
    while index >= 0 and arr[index] > v:
        arr[index+1] = arr[index]
        print_arr(arr)
        index -= 1
    arr[index+1] = v
    print_arr(arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

