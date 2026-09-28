class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]

# In this solution, we use two pointers to find our target
# In our return we increase our left and right index by 1 because the question says the array is 1-indexed
# The array is already sorted so when our total is larger than the target, we just decrease the right pointer and vice versa if it's smaller than the target
# The original Two Sum problem uses a Hash Map to find the target but since this problem wants us to solve it in space complexity O(1) we use two pointers