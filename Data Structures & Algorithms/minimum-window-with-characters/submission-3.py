class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_freq = defaultdict(int)
        for c in t:
            t_freq[c] += 1
        

        freq = defaultdict(int)
        l = 0

        min_length = float("inf")

        need = len(t_freq)
        have = 0
        best = [-1, -1]

        
        for r in range(len(s)):
            char = s[r]
            freq[char] += 1
            
            if char in t_freq and freq[char] == t_freq[char]:
                have += 1

            while have == need:
                if (r - l + 1) < min_length:
                    best = [l, r]
                    min_length = r - l + 1
                
                freq[s[l]] -= 1
                if freq[s[l]] < t_freq[s[l]]:
                    have -= 1
                
                l += 1

        return s[best[0] : best[1] + 1]
                
            



