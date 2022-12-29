from problems.fibonacci import Solution


def test1():
    num = 8
    expected = 21

    sol = Solution()
    assert expected == sol.fibonacci(num)


def test2():
    num = 3
    expected = 2

    sol = Solution()
    assert expected == sol.fibonacci(num)


def test3():
    num = 19
    expected = 4181

    sol = Solution()
    assert expected == sol.fibonacci(num)
