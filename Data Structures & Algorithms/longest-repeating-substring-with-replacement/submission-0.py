class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int) 

        l = 0
        longest = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            
            if (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1  
                l += 1
            
            longest = max(longest, r - l + 1)

        return longest