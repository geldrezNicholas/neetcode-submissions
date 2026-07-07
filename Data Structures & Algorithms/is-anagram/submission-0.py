class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): return False
        dict1 = {}
        dict2 = {}
        for letter1, letter2 in zip(s,t):
            if(letter1 in dict1): dict1[letter1] += 1
            else: dict1[letter1] = 1
            if(letter2 in dict2): dict2[letter2] += 1
            else: dict2[letter2] = 1
        for letter in dict1.keys():
            if(dict2.get(letter) != dict1.get(letter)): return False
        return True