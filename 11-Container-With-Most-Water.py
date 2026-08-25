class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = maxArea = 0
        right = len(height) - 1

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(currentArea, maxArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
            
# In this solution we use two pointers to track the beginning and end of the array
# Every iteration we will move the pointer inward that has the lesser height so we can see potentially larger areas
# The comparison of each iteration also gets a local current Area to compare against the maximum area