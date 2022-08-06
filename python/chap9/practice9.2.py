from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        if len(self.stack):
            return False
        else:
            return True


class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.popleft()

    def isEmpty(self):
        if len(self.queue):
            return False
        else:
            return True


stack = Stack()

poland = ["3", "4", "+", "1", "2", "-", "*"]

operator = ["+", "-", "*", "/"]

for p in poland:
    if p in operator:
        right = stack.pop()
        left = stack.pop()
        formulation = "".join((left, p, right))
        ev = eval(formulation)
        stack.push(str(ev))
    else:
        stack.push(p)

print(stack.pop())
