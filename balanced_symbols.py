class Stack():
    def __init__(self, limit=None):
        self.stk = []
        self.limit = limit

    def is_empty(self):
        return len(self.stk) <= 0

    def push(self, data):
        if len(self.stk) >= self.limit:
            return "Stack Overflow"
        else:
            self.stk.append(data)

    def pop(self):
        if len(self.stk) <= 0:
            return "Stack Underflow", 0
        else:
            return self.stk.pop()

    def size(self):
        return len(self.stk)


def matches(first, second):
    if first == '(' and second == ')':
        return True
    elif first == '{' and second == '}':
        return True
    elif first == '[' and second == ']':
        return True
    else:
        return False


def balanced_symbols(symbols):
    n = len(symbols)
    symbolstack = Stack(n)
    balance = True
    for symbol in symbols:
        if symbol in ['(', '{', '[']:
            symbolstack.push(symbol)
        else:
            if symbolstack.is_empty():
                balance = True
            else:
                ele = symbolstack.pop()
                if matches(ele, symbol):
                    balance = True
                else:
                    balance = False
    f = False if symbolstack.size()>0 else True
    return  balance and f



print(balanced_symbols("{[]{}()[}"))
