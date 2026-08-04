import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # negates the existing values
        max_heap = [-n for n in stones]

        # min-heap the negated values
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # pop 2 largest values
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            # both destroyed
            if x == y: continue 

            # add remains back to heap, negate to maintain priority
            remains = x - y
            heapq.heappush(max_heap, -remains)
        
        # return un-negated remaining value if len = 1 else 0
        return -max_heap[0] if max_heap else 0


