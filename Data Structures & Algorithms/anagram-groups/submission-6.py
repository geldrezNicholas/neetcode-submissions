from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        words = defaultdict(list)

        for string in strs:
            sortString = "".join(sorted(string))
            words[sortString].append(string)
        
        for group in words.values():
            res.append(group)
        
        return res
