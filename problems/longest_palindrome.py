from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            odd = self.expandCenter(s, i, i)
            even = self.expandCenter(s, i, i+1)
            res = max(res, odd, even, key=len)
        return res

    def expandCenter(self, s, left, right):
        while left > 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right]


if __name__ == '__main__':
    print(Solution().longestPalindrome("cbbd"))
