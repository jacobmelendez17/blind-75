class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n+1):
            curr = prev + curr
            prev = curr - prev
            print(f"{curr},{prev}")
        return curr

# In this approach, we use the most space-efficient approach to count number of ways to go up stairs with 1 or 2 steps
# We use two variables to track the current steps of an iteration and then add it to all the previous ones
# With this approach, we get all possibilites to go up the stairs