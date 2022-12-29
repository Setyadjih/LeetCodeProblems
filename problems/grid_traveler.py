"""grid traveler problem, a hidden fibonacci memoization"""


class Solution():
    def __init__(self):
        self.store = {}

    def grid_traveler(self, n, m) -> int:
        if n == 1 or m == 1:
            return 1

        if (n, m) not in self.store.keys():
            self.store[(n, m)] = self.grid_traveler(n-1, m) + self.grid_traveler(n, m-1)

        return self.store[(n, m)]