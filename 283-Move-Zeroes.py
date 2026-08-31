class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return nums

# In this approach we use a two pointer solution where the pointers start as index 0
# We will move the numbers to the left rather than move the zeroes to the right in this solution
# So if we encounter a non-zero we swap our pointers, otherwise the right pointer will keep going
# The left pointer acts as a placement for what will be swapped next in case there is an upcoming zero
# In the event that index 0 is a non-zero, index 0 will 'swap' with itself and both pointers move forward