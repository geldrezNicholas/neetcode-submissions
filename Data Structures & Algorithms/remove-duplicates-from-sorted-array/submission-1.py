class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return 1
        for n in reversed(range(len(nums))):
            if nums[n] == nums[n-1]:
                nums.pop(n)
        return len(nums)