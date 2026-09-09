class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:

            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))

            else:
                t1 = stack.pop()
                t2 = stack.pop()

                if t == "+":
                    stack.append(t2 + t1)

                elif t == "-":
                    stack.append(t2 - t1)

                elif t == "*":
                    stack.append(t2 * t1)

                elif t == "/":
                    stack.append(int(t2 / t1))

        return stack[0]