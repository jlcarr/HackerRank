#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def print_arr(arr):
    print(' '.join(map(str,arr)))

def insertionSort2(n, arr):
    pivot = 1
    while pivot < n:
        pivot_val = arr[pivot]
        i = pivot-1
        while i >= 0 and arr[i] > pivot_val:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = pivot_val
        print_arr(arr)
        pivot += 1

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

