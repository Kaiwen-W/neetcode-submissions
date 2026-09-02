class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += f"{len(s)}#{s}"
        
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        n = ""

        i = 0
        while i < len(s):
            c = s[i]
            if c != "#":
                n += c 
                i += 1
            else:
                n = int(n)
                res.append(s[i+1:i+n+1])

                i += n + 1
                n = ""
                
        return res    
