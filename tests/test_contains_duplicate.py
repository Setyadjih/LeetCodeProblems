from problems.contains_duplicate import Solution


def test1():
    nums = [1,2,3,1]

    sol = Solution()
    assert sol.containsDuplicate(nums)
