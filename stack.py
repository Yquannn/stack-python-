
### STACKS DATA STRUCTURE
class Stack:
    def __init__(self, limit=5):
        self.items = []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.limit

    def push(self, item):
        if self.isFull():
            print('Stack is Full. Cannot push element:', item)
        else:
            self.items.append(item)
            print('Pushed element:', item)

    def pop(self):
        if self.isEmpty():
            print('No Element in Stack')
        else:
            return self.items.pop()

    def peek(self):
        if self.isEmpty():
            print('No Element in Stack')
        else:
            return self.items[0]

    def getLastElement(self):
        if self.isEmpty():
            print('No Element in Stack')
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def availableStack(self):
        return self.limit - self.size()


stack = Stack()


stack.push(10)
stack.push(12)
stack.push(32)
stack.push(21)
stack.pop()
stack.push(100)

print('Current stack:                 ', stack.items)
print('Stack Size:                    ', stack.size())
print('Available stack:               ', stack.availableStack())
print('First Element from the Stack:  ', stack.peek())
print('Last Element from the Stack:   ', stack.getLastElement())
print('Is Stack empty?:               ', stack.isEmpty())
print('Is Stack full?:                ', stack.isFull())