class MinStack:

    def __init__(self):
        self.stack = []
        self.minus_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minus_stack or val <= self.minus_stack[-1]:
            self.minus_stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()

        if self.minus_stack[-1] == popped:
            self.minus_stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minus_stack[-1]