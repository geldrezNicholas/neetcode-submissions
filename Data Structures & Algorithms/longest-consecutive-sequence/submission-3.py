class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        newSet = set(nums)
        longest = 0

        for x in nums:
            if x - 1 not in newSet:
                curr = 1
                while x + curr in newSet:
                    curr += 1
                if curr > longest:
                    longest = curr
                    
        return longest
        



        