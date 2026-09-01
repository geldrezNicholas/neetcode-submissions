class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxHeap = [-i for i in nums]
        heapq.heapify(maxHeap)

        for i in range(1, k+1):
            if i == k:
                return -heapq.heappop(maxHeap)
            heapq.heappop(maxHeap)

