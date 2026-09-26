from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        counts = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in counts:
                return [counts[nums[i]], i]
            counts[target - nums[i]] = i
        
        return []

        