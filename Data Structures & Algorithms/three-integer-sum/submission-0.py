class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = set()

        # go through each element, then for excess numbers do 2 pointers
        # until solution
        for i, n in enumerate(nums):
            # if only 1 element excess, break
            if i > len(nums) - 3:
                break

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = n + nums[l] + nums[r]

                if total == 0:
                    # can use this as check as i <= l <= r for all i, l, r
                    if (n, nums[l], nums[r]) not in res:
                        res.add((n, nums[l], nums[r]))

                    l += 1
                    r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return [list(t) for t in res]
