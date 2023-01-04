class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_p = 0

        start = 0
        end = 1
        while end < len(prices):
            cur_p = prices[end] - prices[start]
            max_p = max(max_p, cur_p)
            if cur_p < 0:
                start = end
                end += 1
            else:
                end += 1

        return max_p


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))