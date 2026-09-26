from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        dictS, dictT = defaultdict(int), defaultdict(int)

        for x, y in zip(s, t):
            dictS[x] += 1
            dictT[y] += 1
        
        return dictS == dictT