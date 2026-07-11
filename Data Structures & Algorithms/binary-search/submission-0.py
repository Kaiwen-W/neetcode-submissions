class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            n = nums[mid]

            if n == target:
                return mid
            elif n < target:
                start = mid + 1 
            else:
                end = mid - 1 

        return -1