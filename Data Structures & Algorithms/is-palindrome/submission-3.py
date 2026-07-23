class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s)-1
        while front < back:
            f = s[front].lower()
            b = s[back].lower()
            
            if f.isalnum() and b.isalnum():
                if f == b:
                    front += 1
                    back -= 1
                else:
                    return False
            elif f.isalnum() and not b.isalnum():
                back -= 1
            elif not f.isalnum() and b.isalnum():
                front += 1
            else:
                front+=1
                back-=1

        return True