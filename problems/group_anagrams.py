from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for letter in strs:
            current = str(sorted(strs))
            hash[current].append(letter)
            

        return list(hash.values())