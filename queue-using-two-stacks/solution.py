# Enter your code here. Read input from STDIN. Print output to STDOUT
class two_stack_queue:
    def __init__(self):
        self.front_stack, self.back_stack = [],[]
    
    def enqueue(self, x):
        self.back_stack.append(x)
    
    def dequeue(self):
        self._flip()
        return self.front_stack.pop()
    
    def peek(self):
        self._flip()
        return self.front_stack[-1]
    
    def _flip(self):
        if not self.front_stack:
            while self.back_stack:
                self.front_stack.append(self.back_stack.pop())
    
queue = two_stack_queue()

q = int(input())
for i in range(q):
    command = input()
    if command.startswith('1'):
        x = command[2:]
        queue.enqueue(x)
    elif command == '2':
        queue.dequeue()
    elif command == '3':
        print(queue.peek())
