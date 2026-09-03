class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((i, temp))
            else:
                (j, val) = stack[-1]
                while temp > val:
                    res[j] = i - j
                    stack.pop()
                    
                    if stack:
                        (j, val) = stack[-1]
                    else:
                        break
                stack.append((i, temp))
        return res