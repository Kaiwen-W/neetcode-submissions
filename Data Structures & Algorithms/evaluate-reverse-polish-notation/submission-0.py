class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }

        stack = []

        for t in tokens:
            if t not in operators.keys():
                stack.append(t)
            else:
                x = stack.pop()
                y = stack.pop()

                stack.append(operators[t](int(x), int(y)))
        
        return stack[0]

