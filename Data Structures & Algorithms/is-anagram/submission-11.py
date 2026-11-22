from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for x, y in zip(s, t):
            d1[x] += 1
            d2[y] += 1
        
        return d1 == d2
        
