class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        # store as value:index

        for i, n in enumerate(nums):
            d = target - n 
            if d in seen:
                return [seen[d], i]
            seen[n] = i 
        