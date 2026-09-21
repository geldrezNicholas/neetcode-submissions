class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        newSet = set(nums)
        longest = 0

        for x in nums:
            if x - 1 not in newSet:
                currLength = 1
                while (x + currLength) in newSet:
                    currLength += 1
                if longest < currLength:
                    longest = currLength
        return longest
        


        