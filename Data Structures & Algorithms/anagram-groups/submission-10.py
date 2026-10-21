from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        words = defaultdict(list)

        for string in strs:
            words[''.join(sorted(string))].append(string)
        
        for word, wordList in words.items():
            res.append(wordList)
        
        return res

