class MinStack:

    def __init__(self):
        self.stack = []
        self.min_idx_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_idx_stack) == 0 or self.stack[self.min_idx_stack[-1]] >= val:
            self.min_idx_stack.append(len(self.stack) - 1)

    def pop(self) -> None:
        self.stack.pop()
        if self.min_idx_stack and self.min_idx_stack[-1] == len(self.stack):
            self.min_idx_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.stack[self.min_idx_stack[-1]]
        
