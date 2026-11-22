from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        counts = defaultdict(list)

        for string in strs:
            sortedString = "".join(sorted(string))
            counts[sortedString].append(string)
        
        return list(counts.values())

