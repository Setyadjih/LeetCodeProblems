from collections import deque


class MinStack:

    def __init__(self):
        self.val_stack = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        self.val_stack.appendleft(val)
        if not self.min_stack:
            self.min_stack.appendleft(val)
        else:
            self.min_stack.appendleft(min(val, self.getMin()))

    def pop(self) -> None:
        self.val_stack.popleft()
        self.min_stack.popleft()

    def top(self) -> int:
        return self.val_stack[0]

    def getMin(self) -> int:
        return self.min_stack[0]
