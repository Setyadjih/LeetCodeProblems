from problems.fibonacci import Solution


def test1():
    num = 8
    expected = 21

    sol = Solution()
    assert expected == sol.fib1(num)


def test2():
    num = 3
    expected = 2

    sol = Solution()
    assert expected == sol.fib1(num)


def test3():
    num = 50
    expected = 12586269025

    sol = Solution()
    assert expected == sol.fib1(num)
