class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs, stack = [], []

        for x in range(len(speed)):
            pairs.append([position[x], speed[x]])

        pairs = sorted(pairs)[::-1]

        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

# In this solution, we use a stack that stores the calculations of how long it will take each car to get to the target
# We start by creating our stack and a list that stores list pairs of every car's position and speed
# We sort this array in descending order of position so that we can compare car fleets
# The formular on line 11 gives us the time it takes for a car to get to the target. We add that to the stack
# If the pair in the stack before is larger, it means it takes a longer time for that car therefore it joins that fleet so we pop it
# However many pairs are in the stack is how many car fleets we have