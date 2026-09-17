class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokenStack = []
        for token in tokens:
            if token == "/" or token == "*" or token == "+" or token == "-":
                y = tokenStack.pop()
                x = tokenStack.pop()
                if token == "/":
                    result = int(x / y)
                elif token == "*":
                    result = x * y
                elif token == "+":
                    result = x + y
                elif token == "-":
                    result = x - y
                tokenStack.append(int(result))
            else:
                tokenStack.append(int(token))
        return tokenStack.pop()