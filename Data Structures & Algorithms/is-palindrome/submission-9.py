class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            l = s[left]
            r = s[right]

            if not l.isalnum():
                left += 1
                continue
            if not r.isalnum():
                right -= 1
                continue
            
            if l.lower() != r.lower():
                return False
            
            left += 1
            right -= 1
        
        return True
