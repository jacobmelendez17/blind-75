class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        results = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                results[index] = i - index
            stack.append(i)
        return results

# In this solution we use a stack to keep track of temperature indices
# For every temperature, we check if our stack exists (to see if it even has a comparison)
# We also check if the the top of our stack is less than the current temperature meaning a warmer temperature has been found
# If it is, we pop the index of the warmer temperature off the stack and subtract it from our current index to get the distance/days
# Then we append our current temperature to the stack once we find the largest day difference from the stack