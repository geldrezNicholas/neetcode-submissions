from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        final = []
        dic = defaultdict(list)

        for string in strs:
            dic["".join(sorted(string))].append(string)

        for word, group in dic.items():
            final.append(group)
        
        return final