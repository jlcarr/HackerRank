#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    # construct the graph, adjacency-list style
    G = {i:set() for i in range(1,n+1)}
    for e in edges:
        G[e[0]].add(e[1])
        G[e[1]].add(e[0])
    
    queue = [s]
    found = {s:0}
    while queue:
        curr = queue.pop(0)
        for e in G[curr]:
            if e not in found:
                found[e] = 1 + found[curr]
                queue.append(e)
    return [6*found[i] if i in found else -1 for i in range(1,n+1) if i != s]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

