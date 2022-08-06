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


input_seq = "(()(())())(()())"
stack = Stack()

i_pair = []
judge = True

for i, c in enumerate(input_seq):
    if c == "(":
        stack.push((i, c))
    else:
        sc = stack.pop()
        if sc[1] == ")" or stack.isEmpty():
            judge = False
            break
        else:
            i_pair.append((sc[0], i))

print(judge, i_pair)
