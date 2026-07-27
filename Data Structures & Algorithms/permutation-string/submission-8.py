class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = [0] * 26
        for c in s1:
            perm[ord(c) - ord('a')] += 1
        
        # setup sliding window
        k = len(s1)
        l = 0
        freq = [0] * 26

        for r in range(len(s2)):
            char = s2[r]

            freq[ord(char) - ord('a')] += 1

            if sum(freq) == k:
                if freq == perm:
                    return True
                
                freq[ord(s2[l]) - ord('a')] -= 1
                l += 1 

        return False
                

