class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        # since nums is sorted if nums[i] + total > target
        # then nums[i + 1] + total also > target
        # prune from there
        nums.sort() # O(nlog n)

        res = []

        def backtrack(start: int, current_path: List[int], total: int) -> None:
            if total == target:
                res.append(current_path.copy())
                return # since no more numbers can be added
            
            for i in range(start, len(nums)):
                choice = nums[i]

                if total + choice > target:
                    break
                
                # prevent duplicate subtrees
                if i > start and nums[i] == nums[i - 1]:    
                    continue
                
                current_path.append(choice)
                backtrack(i + 1, current_path, total + choice)

                current_path.pop()
        
        backtrack(0, [], 0)

        return res


            

