class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = set(nums)

        longest_len = 0
        for n in nums:
            if (n - 1) in nums:
                continue

            cur_len = 1
            next_num = n + 1 

            while next_num in nums:
                cur_len += 1 
                next_num += 1 
            
            if cur_len > longest_len:
                longest_len = cur_len

        return longest_len