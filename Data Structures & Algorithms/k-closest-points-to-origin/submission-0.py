from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max-heap

        points = [[-sqrt(x ** 2 + y ** 2), [x, y]] for x, y in points]

        heapq.heapify(points) # O(n)

        while len(points) > k:
            heapq.heappop(points)
        
        return [pairs[1] for pairs in points]