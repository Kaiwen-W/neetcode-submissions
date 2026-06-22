class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l < r:
            left = nums[l]
            right = nums[r]

            if (left + right) == target:
                return [l + 1, r + 1]
            elif (left + right) > target:
                r -= 1
            else:
                l += 1