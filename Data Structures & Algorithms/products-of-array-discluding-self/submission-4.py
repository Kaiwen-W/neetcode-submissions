class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [0 for _ in range(len(nums) - 1)]
        post.append(1)
        
        # prefix product 
        prod = 1
        for i in range(len(nums) - 1):
            prod *= nums[i]
            pre.append(prod)

        # post product
        prod = 1
        for i in range(len(nums) - 1, 0, -1):
            prod *= nums[i]
            post[i - 1] = prod


        return [pre[i] * post[i] for i in range(len(nums))]
