class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(start_index, current_path):
            if tuple(current_path) not in res:
                res.add(tuple(current_path))
            
            for i in range(start_index, len(nums)):
                choice = nums[i]

                if choice in current_path:
                    continue
                
                current_path.append(choice)
                backtrack(i + 1, current_path) 
                current_path.pop()

        backtrack(0, [])
        return [list(sub) for sub in res]


                
