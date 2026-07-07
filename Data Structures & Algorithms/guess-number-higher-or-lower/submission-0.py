# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        L, H = 0, n

        while L <= H:
            M = (L+H)//2

            if guess(M) > 0:
                L = M+1
            elif guess(M) < 0:
                H = M-1
            else:
                return M