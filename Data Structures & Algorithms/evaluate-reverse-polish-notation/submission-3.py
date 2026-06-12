class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            try:
                stack.append(int(s))
            except ValueError:
                second = stack.pop()
                first = stack.pop()
                if s == "+":
                    stack.append( first + second )
                elif s == "-":
                    stack.append( first - second )
                elif s == "*":
                    stack.append( first * second )
                elif s == "/":
                    stack.append( int(first / second) )
        return math.floor(stack[0])
