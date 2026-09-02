class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = set()
        for n in nums:
            seen.add(n)
        
        # only consider numbers which have nothing before it as the start

        longest = 1
        curr = 1

        for n in nums:
            if (n - 1) in seen:
                continue
            
            count = 1
            while True:
                if (n + count) in seen:
                    curr += 1
                    longest = max(longest, curr)
                    count += 1
                else:
                    curr = 1 
                    break
        
        return longest
