class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if s == s[::-1]:
            return s
        longest = ""

        # find the longest palindrome from each letter as the center
        # do again for even sized palindromes
        for i in range(len(s)):
            start = i
            end = i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if (end - start + 1) > len(longest):
                    longest = s[start:end+1]

                start -= 1
                end += 1

            start, end = i, i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                # get length of palindrome
                if (end - start + 1) > len(longest):
                    longest = s[start:end + 1]

                start -= 1
                end += 1

        return longest

if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"))