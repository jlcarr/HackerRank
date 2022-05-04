# HackerRank
Solutions to HackerRank problems in Python3

## Results
### Problem: A Very Big Sum
- **Link**: https://www.hackerrank.com/challenges/a-very-big-sum/problem
- **Solution**: Use Python's built-in sum function.

### Problem: Arrays: Left Rotation
- **Link**: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
- **Solution**: Use Python's array slicing and concatenation.

### Problem: Insert a node at a specific position in a linked list
- **Link**: https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
- **Solution**: Keep track of previous and subsequent nodes in the linked list and iterate through to find the insert position.

### Problem: Cycle Detection
- **Link**: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
- **Solution**: Tortoise and Hare algorithm.

### Problem: Balanced Brackets
- **Link**: https://www.hackerrank.com/challenges/balanced-brackets/problem
- **Solution**: Keep a stack, also used a dict to map opening to closing brackets.

### Problem: Queue using Two Stacks
- **Link**: https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
- **Solution**: One stack represents the end of the queue, and the other the front. When a value from the front is needed but is empty, the back is popped into the front, effectively flipping the stack.

### Problem: Ice Cream Parlor
- **Link**: https://www.hackerrank.com/challenges/icecream-parlor/problem
- **Solution**: Used a dict to store the indices of last occurance of each value. Then easily look up the complement of each value in the dict and check for distinct indices.

### Problem: Insertion Sort - Part 1
- **Link**: https://www.hackerrank.com/challenges/insertionsort1/problem
- **Solution**: Simply iterate down the array.

### Problem: Insertion Sort - Part 2
- **Link**: https://www.hackerrank.com/challenges/insertionsort2/problem
- **Solution**: Iterate through the array, each time running the routine from Insertion Sort - Part 1.

### Problem: Binary Search Tree : Insertion
- **Link**: https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
- **Solution**: Classic binary search tree: traverse down the tree until a missing leaf is found.

### Problem: Tree: Height of a Binary Tree
- **Link**: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
- **Solution**: Recursively compute the height, taking of the max of each search path at each level of recursion. The base case for leaves being 0.

### Problem: Breadth First Search: Shortest Reach
- **Link**: https://www.hackerrank.com/challenges/bfsshortreach/problem
- **Solution**: Simple BFS, used a Python list as a queue. Kept a dict mapping found values to their depths.

### Problem: Snakes and Ladders: The Quickest Way Up
- **Link**: https://www.hackerrank.com/challenges/the-quickest-way-up/problem
- **Solution**: Dijkstra's algorithm, with Python's heapq to implement the priority queue.

### Problem: 
- **Link**: 
- **Solution**: 

