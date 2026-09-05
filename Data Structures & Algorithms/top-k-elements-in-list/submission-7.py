from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if not nums or k == 0:
            return []

        counter = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counter[num] += 1

        for num, count in counter.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            if len(res) == k:
                return res
            for j in freq[i]:
                res.append(j)
        
        return res
        

        
