import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # negates the existing values
        max_heap = [-n for n in stones]

        # min-heap the negated values
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x == y: continue 

            remains = x - y
            heapq.heappush(max_heap, -remains)
        
        return -max_heap[0] if max_heap else 0


