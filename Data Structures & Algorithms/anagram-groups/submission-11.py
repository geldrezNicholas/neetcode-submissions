from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        dic = defaultdict(list)

        for string in strs:
            sortedString = "".join(sorted(string))
            dic[sortedString].append(string)
        
        for word, array in dic.items():
            res.append(array)
        
        return res
            
