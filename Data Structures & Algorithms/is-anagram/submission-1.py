from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)

        for l1, l2 in zip(s, t):
            dic1[l1] += 1
            dic2[l2] += 1
        
        return dic1 == dic2
        
        

