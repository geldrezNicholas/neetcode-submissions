from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)

        for x, y in zip(s, t):
            dic1[x] += 1
            dic2[y] += 1
        
        return dic1 == dic2