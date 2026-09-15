class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0
        for n in my_set:
            if n - 1 not in my_set:
                length = 1
                while n + length in my_set:
                     length += 1
                longest = max(longest, length)
        return longest

# In this solution, we use a set to track numbers to keep our solution O(n)
# For every number that doesn't have a subsequent number, we create a new length to check how long its sequence is
# We do this by checking n - 1 because the n with n - 1 will be the start of a sequence every time
# As long as there is a consecutive number in the set we add to the length and then compare to the longest length