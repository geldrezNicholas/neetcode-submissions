from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        ct1 = defaultdict(int)
        ct2 = defaultdict(int)

        for x,y in zip(s,t):
            ct1[x] += 1
            ct2[y] += 1

        return ct1 == ct2


