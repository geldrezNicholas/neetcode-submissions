class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        for n in range(len(s)):
            if s[n] in ('(', '[', '{'):
                stack.append(s[n])
            if len(stack) in (len(s), 0):
                return False
            else:
                if s[n] == '}' and stack.pop() != '{':
                    return False
                elif s[n] == ']' and stack.pop() != '[':
                    return False
                elif s[n] == ')' and stack.pop() != '(':
                    return False
        if len(stack) == 0:
            return True
        else:
            return False