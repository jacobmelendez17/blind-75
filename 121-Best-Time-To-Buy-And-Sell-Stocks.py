class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit

# In this solution we use a variant of Kadane's Algorithm (finds max subarray sum in array)
# In our approach, we use dynamic programming to check the best stock
# We set our buying stock to the first element
# For every element we check if that element is less than our current buy variable which would be most ideal (profitable)
# If it's not we also check if selling that current item with our current buy variable will be most profitable
# If it's neither we just move on and return the profit