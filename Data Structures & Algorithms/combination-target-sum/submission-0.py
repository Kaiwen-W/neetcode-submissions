class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start_index, current_path):
            if sum(current_path) == target:
                res.append(current_path.copy())
                return 
            
            for i in range(start_index, len(nums)):
                if sum(current_path) > target:
                    continue
                
                current_path.append(nums[i])
                backtrack(i, current_path)
                current_path.pop()
            
        backtrack(0, [])
        return res