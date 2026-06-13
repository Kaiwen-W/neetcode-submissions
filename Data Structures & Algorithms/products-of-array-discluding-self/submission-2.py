class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = math.prod(nums)
        no_0_prod = math.prod([n for n in nums if n != 0])

        num_0 = 0
        for n in nums:
            if n == 0:
                num_0 += 1

        res = []

        for num in nums:
            if num == 0:
                if num_0 == 1:
                    res.append(no_0_prod)
                else:
                    res.append(0)
            else:
                res.append(int(prod/num))

        return res