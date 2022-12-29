"""Think about memoization"""


class Solution:
    def __init__(self):
        # Save your results, since we calculate the same results multiple times
        self.store = {}

    def fib1(self, n):
        if n <= 2:
            return 1
        if n not in self.store.keys():
            self.store[n] = self.fib1(n - 1) + self.fib1(n - 2)

        return self.store[n]
