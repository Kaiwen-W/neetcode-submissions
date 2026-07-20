class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for c in s:
            s_dict[c] += 1 
        
        for c in t:
            t_dict[t] += 1 
        
        for key in s_dict:
            if s_dict[key] != t_dict[key]:
                return False
        return True
                