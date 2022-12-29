class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # go over each item, with increasingly shorter list
        for i, num in enumerate(nums):
            rem = target - num
            index_others = i+1

            others = nums[index_others:]
            if rem in others:
                return [i, others.index(rem) + i + 1]


