from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        words = defaultdict(list)
        for word in strs:
            sortedWord = sorted(word)
            words[''.join(sortedWord)].append(word)
        
        for duo in words.items():
            final.append(duo[1])
        
        return final

