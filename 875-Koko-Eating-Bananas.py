class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def canFinish(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += pile // k
                if pile % k != 0:
                    hours += 1
                if hours > h:
                    return False
            return True

        left, right = 1, max(piles)
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            if canFinish(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

# In this solution, we use binary search to find the minimum rate of eating bananas, k
# We know the minimum of k must be 1 and maximum must be the largest pile size, so we find our first mid based on these values
# We use a helper function to check if the eating rate will be higher or less than the hours by adding the hours it takes to eat each pile with k
# We add the rate and if there are remaining bananas, we add an extra hour to our total
# If the rate works, we move our right down to see if there's a smaller rate
# If it doesn't work, we need to move the left because we are going too slow