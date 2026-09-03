class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operate(x: int, y: int, op: str) -> int:
            if op == "+":
                return x + y
            elif op == "-":
                return x - y
            elif op == "/":
                return int(x / y)
            else:
                return x * y
        
        stack = []
        ops = set("+-*/")

        for t in tokens:
            if t not in ops:
                stack.append(t)
            else:
                y = stack.pop()
                x = stack.pop()

                stack.append(operate(int(x), int(y), t))
        
        return int(stack[0])
