class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        n = len(nums)
        for x in range(n):
            complement = target - nums[x]
            if complement in my_map:
                return [my_map[complement], x]
            my_map[nums[x]] = x

# For this solution we use a hash map to store any numbers we have already seen that doesn't have a complement yet
# Once we find a match, we return the index of the complement and current index
# This only takes O(n) time since we store numbers in a hash map and check quicker that way