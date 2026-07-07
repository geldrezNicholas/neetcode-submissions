class MinStack:

    def __init__(self):
        self.MinStack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.MinStack.append(val)
        val = min(val, self.stack[-1] if self.stack else val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.MinStack.pop()

    def top(self) -> int:
        return self.MinStack[-1]

    def getMin(self) -> int:
        return self.stack[-1]
