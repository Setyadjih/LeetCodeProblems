from problems.grid_traveler import Solution


def test_grid_traveler1():
    n = 2
    m = 3
    e = 3

    sol = Solution()
    assert sol.grid_traveler(n, m) == e


def test_grid_traveler2():
    n = 3
    m = 2
    e = 3

    sol = Solution()
    assert sol.grid_traveler(n, m) == e


def test_grid_traveler3():
    n = 3
    m = 3
    e = 6

    sol = Solution()
    assert sol.grid_traveler(n, m) == e


def test_grid_traveler4():
    n = 18
    m = 18
    e = 2333606220

    sol = Solution()
    assert sol.grid_traveler(n, m) == e

