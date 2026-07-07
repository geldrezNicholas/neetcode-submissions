class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L,R = 1, max(piles)
        sol = R
        while L <= R:
            k = (R+L)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            
            if hours <= h:
                sol = k
                R = k-1 
            else: 
                L = k + 1
        return sol