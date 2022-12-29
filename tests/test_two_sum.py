from problems.two_sum import Solution


def core(nums, target, expected):
    sol = Solution()
    result = sol.twoSum(nums, target)
    assert result == expected


def test1():
    core([2, 7, 11, 15], 9, [0, 1])


def test2():
    core([3, 2, 4], 6, [1, 2])


def test3():
    core([3, 3], 6, [0, 1])
