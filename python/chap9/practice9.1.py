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


s = Stack()
print(s.isEmpty())
s.push(2)
s.push(3)
print(s.pop())
print(s.isEmpty())


q = Queue()
print(q.isEmpty())
q.push(2)
q.push(3)
print(q.pop())
print(q.isEmpty())
