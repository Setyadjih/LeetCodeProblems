class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(" ")
        new = []
        for w in words:
            if len(w) <= 2:
                new.append(w.lower())
            else:
                new.append(w.lower().capitalize())
        return " ".join(new)