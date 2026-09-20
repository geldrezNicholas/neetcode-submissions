from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in res:
                return [res[nums[i]], i]
            res[target - nums[i]] = i
        
        return []
