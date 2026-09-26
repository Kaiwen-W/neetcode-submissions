class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        close_to_open = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c not in close_to_open:
                stack.append(c)
            else:
                if not stack:
                    return False

                end = stack.pop()

                if close_to_open[c] != end:
                    return False
        
        return len(stack) == 0