class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {"(": ")", "{": "}", "[": "]"}
        opening = set(["{", "(", "["])
        
        if s[0] not in opening or len(s) % 2 == 1:
            return False

        stack = [s[0]]

        for i in range(1, len(s)):
            c = s[i]
            if c in opening:
                stack.append(c)
                continue
            
            last = stack.pop()

            if c != paren_map[last]:
                return False

        if len(stack) != 0:
            return False

        return True