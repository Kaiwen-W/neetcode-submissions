class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = math.prod(nums)

        res = []

        for num in nums:
            if num == 0:
                res.append(math.prod([n for n in nums if n != 0]))
            else:
                res.append(int(prod/num))

        return res