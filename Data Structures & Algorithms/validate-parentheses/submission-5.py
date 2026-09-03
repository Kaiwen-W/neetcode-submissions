class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        paren_map = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for c in s:
            if c not in paren_map.keys():
                stack.append(c)
            # closing bracket
            else:
                if not stack:
                    return False
                
                last = stack.pop()

                if paren_map[c] != last:
                    return False
        if stack:
            return False
        return True