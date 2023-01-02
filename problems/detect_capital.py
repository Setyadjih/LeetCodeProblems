class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # All caps
        if word == word.upper():
            return True

        # no caps
        if word == word.lower():
            return True

        # 1 caps
        if word.capitalize() == word:
            return True

        return False
