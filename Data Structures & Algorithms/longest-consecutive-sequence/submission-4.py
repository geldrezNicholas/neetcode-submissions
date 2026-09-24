class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        newSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in newSet:
                currLongest = 1
                while num + 1 in newSet:
                    currLongest += 1
                    num += 1
                if currLongest > longest:
                    longest = currLongest
        
        return longest


        



        