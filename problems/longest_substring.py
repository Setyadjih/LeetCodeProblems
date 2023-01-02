class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs_max = ""
        curr_max = ""
        for n in s:
            if n not in curr_max:
                curr_max += n
                if len(curr_max) > len(subs_max):
                    subs_max = curr_max
            else:
                first_occur = curr_max.index(n)
                curr_max = curr_max[first_occur+1:] + n

        return len(subs_max)


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("ggububgvfk"))
