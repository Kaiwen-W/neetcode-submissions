class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        state = {} # char -> index

        for r in range(len(s)):
            char = s[r]

            if char in state:                
                l = max(state[char] + 1, l)

            state[char] = r
            res = max(res, r - l + 1)

        return res