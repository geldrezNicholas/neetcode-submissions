class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            if x == y:
                continue
            elif x > y:
                heapq.heappush(maxHeap, y-x)
        
        if len(maxHeap) > 0:
            return -maxHeap[0]
        else:
            return 0