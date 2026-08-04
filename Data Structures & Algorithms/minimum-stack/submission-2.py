class MinStack:

    def __init__(self):
        self.min_val = None
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min_val is None:
            self.min_val = val
        elif val < self.min_val:
            self.min_val = val
        
        self.min_stack.append(self.min_val)

    def pop(self) -> None:
        popped_val = self.stack.pop()
        popped_min = self.min_stack.pop()
        
        if self.min_stack:
            self.min_val = self.min_stack[-1]
        else:
            self.min_val = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
