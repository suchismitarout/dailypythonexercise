class Stack():
    def __init__(self, limit=10):
        self.stk = []
        self.limit = limit

    def stk_is_empty(self):
        return len(self.stk) <= 0

    def push(self, item):
        if len(self.stk) >= self.limit:
            return "Stack Overflow"
        else:
            self.stk.append(item)
            return "after push", self.stk

    def pop(self):
        if len(self.stk) <= 0:
            return "Stack Underflow", 0
        else:
            self.stk.pop()
            return "after pop", self.stk

    def peek(self):
        if len(self.stk) <= 0:
            return "Stack Underflow", 0
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)


stack = Stack(4)
stack.push(2)
stack.push(3)
print(stack.push(5))
print(stack.push(10))
print(stack.push(11))
print(stack.size())
print(stack.pop())
print(stack.size())
print(stack.peek())