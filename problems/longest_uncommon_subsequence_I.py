from collections import Counter

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # exactly the same
        if a == b:
            return -1

        return max(len(a), len(b))


if __name__ == '__main__':
    res = Solution().findLUSlength("aba", "cdc")
    print(res)
