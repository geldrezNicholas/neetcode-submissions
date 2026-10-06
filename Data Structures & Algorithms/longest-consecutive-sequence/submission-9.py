class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        newSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in newSet:
                currLength = 1
                while (num + currLength) in newSet:
                    currLength += 1
                longest = max(currLength, longest)
        
        return longest



        