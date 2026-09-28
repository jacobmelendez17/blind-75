class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                second, first = stack.pop(), stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(c))
        return stack[0]
# In this solution we utilize a stack to keep track of what numbers go into the operations
# Numbers are pushed into the stack and when an operation shows up, we do that operation on the last two popped numbers and push the answer to the stack
# For subtraction and division, order matters so we assign variables for the first and second pop
# Since our original list contains strings and we need to do floor operations for divisions we use int conversion there