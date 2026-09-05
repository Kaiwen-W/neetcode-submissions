class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums) # min heap

        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        return heapq.nlargest(self.k, self.nums)[-1] 
        
