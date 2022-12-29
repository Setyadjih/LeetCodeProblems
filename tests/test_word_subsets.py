"""Test your solution and check how you're doing"""
from problems.word_subsets import Solution


def test1():
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["e", "o"]
    expected = ["facebook", "google", "leetcode"]

    sol = Solution()
    result = sol.wordSubsets(words1, words2)
    assert result == expected


def test2():
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["l", "e"]
    expected = ["apple","google","leetcode"]

    sol = Solution()
    result = sol.wordSubsets(words1, words2)
    assert result == expected

def test3():
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["e", "oo"]
    expected = ["facebook","google"]

    sol = Solution()
    result = sol.wordSubsets(words1, words2)
    assert result == expected

def test4():
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["lo","eo"]
    expected = ["google","leetcode"]

    sol = Solution()
    result = sol.wordSubsets(words1, words2)
    assert result == expected