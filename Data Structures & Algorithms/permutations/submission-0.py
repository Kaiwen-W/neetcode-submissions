class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(start, current_path):
            if len(current_path) == len(nums):
                res.append(current_path.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in current_path:
                    continue

                current_path.append(nums[i])
                backtrack(i + 1, current_path)
                current_path.pop()
        
        backtrack(0, [])

        return res
