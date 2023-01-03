class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s_num = str(x)
        rev = s_num[::-1]

        return s_num == rev


if __name__ == '__main__':
    res = Solution().isPalindrome(-121)
    print(res)
