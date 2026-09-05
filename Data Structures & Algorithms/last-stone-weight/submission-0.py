class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use max heap

        heap = [-x for x in stones]
        heapq.heapify(heap) # O(n)

        while len(heap) > 1:
            y = -(heapq.heappop(heap))
            x = -(heapq.heappop(heap))

            if x == y:
                continue
            else:
                heapq.heappush(heap, -(y - x))
        
        if len(heap) == 1:
            return -heap[0]
        else:
            return 0
