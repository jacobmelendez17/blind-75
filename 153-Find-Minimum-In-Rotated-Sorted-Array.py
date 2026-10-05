from ast import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

# In this solution, we use binary search to find the minimum
# After getting our middle, we check if the middle is less than the right
# If it is, we know the minimum must be on the left side because the right side is sorted
# If the middle is greater than the right, we know the minimum must be on the right because the left side is sorted