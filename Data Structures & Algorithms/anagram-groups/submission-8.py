from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        words = defaultdict(list)

        for string in strs:
            sortedString = "".join(sorted(string))
            words[sortedString].append(string)

        for wordList in words.values():
            res.append(wordList)

        return res