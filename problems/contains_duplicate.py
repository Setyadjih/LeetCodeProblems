from collections import Counter

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        count = Counter(nums)
        highest = count.most_common(1)[0]
        return highest[1] > 1