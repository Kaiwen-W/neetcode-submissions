class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for c in s:
            if s_dict[c]: 
                s_dict[c] += 1 
            else:
                s_dict[c] = 1 
        
        for c in t:
            if t_dict[c]: 
                t_dict[c] += 1 
            else:
                t_dict[c] = 1
        
        for key in s_dict:
            if s_dict[key] != t_dict[key]:
                return False
        return True
                