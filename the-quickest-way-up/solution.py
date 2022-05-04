#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

def quickestWayUp(ladders, snakes):
    # parse_movers
    movers = dict()
    for e in ladders:
        movers[e[0]] = e[1]
    for e in snakes:
        movers[e[0]] = e[1]
        
    # (estimated_cost, cost_so_far, positon)
    costs = dict()
    costs[1] = 0
    
    queue = [(0,1)]
    while queue:
        cost, pos = heapq.heappop(queue)
        if cost > costs[pos]:
            continue
        for i in range(1,6+1):
            new_pos = pos + i
            if new_pos > 100:
                continue
            if new_pos in movers:
                new_pos = movers[new_pos]
            #while new_pos in movers:
            #    new_pos = movers[new_pos]
            if new_pos not in costs or cost + 1 < costs[new_pos]:
                costs[new_pos] = cost + 1
                heapq.heappush(queue, (cost + 1, new_pos))
    #print(costs)
    if 100 not in costs:
        return -1
    return costs[100]
                
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()

