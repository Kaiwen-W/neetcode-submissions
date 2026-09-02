class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for c in s:
            s_dict[c] += 1
        
        for c in t:
            t_dict[c] += 1
        
        for c in s_dict.keys():
            if t_dict[c] != s_dict[c]:
                return False
        
        return True