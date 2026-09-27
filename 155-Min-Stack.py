class MinStack:

    def __init__(self):
        self.s = []

    def push(self, value: int) -> None:
        if not self.s:
            self.s.append((value, value))
        else:
            curr_min = min(value, self.s[-1][1])
            self.s.append((value, curr_min))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# In this soluton we need to do all operaitons in constant time
# Python does not have its own stack data structure so we will use a a list with tuples to track the value and minimum value
# In push, we if the stack is not empty we check the last appended minimum value and compare it to our current value being pushed
# In top, we return the last appended value and in getMin we return the last appended minimum value