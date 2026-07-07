class MinStack:

    def __init__(self):
        self.MinStack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.MinStack.append(val)
        if self.stack:
            if self.stack[-1] < val :
                val = self.stack[-1]
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.MinStack.pop()

    def top(self) -> int:
        return self.MinStack[-1]

    def getMin(self) -> int:
        return self.stack[-1]
