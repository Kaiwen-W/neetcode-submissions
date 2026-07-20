class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += s
            res += " "
        return res

    def decode(self, s: str) -> List[str]:
        if len(s) == 1:
            return [""]
        return s.split()