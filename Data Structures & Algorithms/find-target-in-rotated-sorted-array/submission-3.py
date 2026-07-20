class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first find where pivot (minimum value) is
        pivot = (nums[0], 0) # value, index

        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                pivot = min(pivot, (nums[l], l))
                break
            
            mid = (l + r) // 2
            pivot = min(pivot, (nums[mid], mid))
            if nums[r] < nums[mid]: 
                l = mid + 1
            else:
                r = mid - 1

        # print(pivot)
        
        def binary_search(nums, target, l, r): 
            while l <= r:
                mid = (l + r) // 2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return -1 

        # then do another binary search to find the target
        if pivot[1] == 0:
            max_i = len(nums) - 1
        else:
            max_i = pivot[1] - 1

        if nums[0] <= target and target <= nums[max_i]:
            return binary_search(nums, target, 0, max_i)
        else:
            return binary_search(nums, target, max_i, len(nums) - 1)



