class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[l] < nums[r]:
                return nums[l]
            elif nums[l] < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
