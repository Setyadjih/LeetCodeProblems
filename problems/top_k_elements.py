class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = [[] for x in range(len(nums) + 1)]
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            res.extend(freq[i])
            if len(res) == k:
                return res

if __name__ == '__main__':
    print(Solution().topKFrequent(nums = [1], k = 1))

