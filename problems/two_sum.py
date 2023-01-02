class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i, n in enumerate(nums):
            remainder = target - n
            if remainder in num_map:
                return [num_map[remainder], i]
            num_map[nums[i]] = i


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))
