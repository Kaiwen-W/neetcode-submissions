class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        # go through each element, then for excess numbers do 2 pointers
        # until solution
        for i, n in enumerate(nums):
            # if only 1 element excess, or excess numbers positive, break
            if i > len(nums) - 3 or n > 0:
                break

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = n + nums[l] + nums[r]

                if total == 0:
                    res.append([n, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return res
