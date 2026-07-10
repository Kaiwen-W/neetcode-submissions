class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y),
        }

        stack = []

        for t in tokens:
            if t not in operators.keys():
                stack.append(int(t))
            else:
                y = stack.pop()
                x = stack.pop()

                stack.append(operators[t](x, y))
        
        return stack[0]

