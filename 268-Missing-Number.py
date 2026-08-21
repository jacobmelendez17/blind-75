class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        real_sum = (n * (n + 1)) // 2
        sub_sum = sum(nums)
        return real_sum - sub_sum
    
# In this solution we compare the sum of what all the actual numbers should be to the sum of what we have
# We use the Gauss formula to find the actual sum of numbers from 0 to n
# We then subtract the sum of numbers we have in our array to the real sum