class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
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
                total += choice

                if total > target:
                    break
                
                current_path.append(choice)
                # we do i and not i + 1, since we can use each num
                # unlimited amount of times
                backtrack(i, current_path, total)

                total -= choice
                current_path.pop()
        
        backtrack(0, [], 0)

        return res


            

