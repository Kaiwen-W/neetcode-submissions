class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[l] > nums[r]:
                if nums[l] < nums[mid] < nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                return nums[l] - 1 