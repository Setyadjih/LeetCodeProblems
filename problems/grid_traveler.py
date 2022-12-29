"""grid traveler problem, a hidden fibonacci memoization. this one implemented with store in function"""


class Solution():
    def grid_traveler(self, n, m, store=None) -> int:
        if store is None:
            store = {}

        if n == 1 or m == 1:
            return 1

        # f(a, b) == f(b, a)! since a grid in either shape is the same
        if (n, m) not in store.keys() or (m, n) not in store.keys():
            store[(n, m)] = self.grid_traveler(n-1, m, store) + self.grid_traveler(n, m-1, store)
            store[(m, n)] = store[(n, m)]

        if (n, m) in store.keys():
            return store[n, m]
        else:
            return store[m, n]
