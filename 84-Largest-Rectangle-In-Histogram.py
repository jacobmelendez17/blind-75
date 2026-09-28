class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        #heights.pop()
        return ans

# In this solution, we will use a stack to keep track of indeces to help us get the width of the largest rectangle
# We start by appending a 0 to our original heights list. This helps us do an extra calculation at the end for what's leftover
# We add -1 to the bottom of the stack to help us track our width by providing an imaginary index that will provide the correct width even when our rectangle reaches all the way to index 0
# In the loop, we check if our current height is smaller than the ones in the stack. If it is, we find the max rectangle based on our minimum height and if it's our largest we store it
# The pop method is just there for cleanup. It is not needed for the final return