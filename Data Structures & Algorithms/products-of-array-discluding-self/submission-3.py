class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # try and solve with no division operation


        prod = math.prod(nums)

        num_0 = 0
        for n in nums:
            if n == 0:
                num_0 += 1

        res = []

        for num in nums:
            if num == 0:
                if num_0 == 1:
                    res.append(math.prod([n for n in nums if n != 0]))
                else:
                    res.append(0)
            else:
                res.append(int(prod/num))

        return res