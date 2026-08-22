class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_map = {}
        for num in nums:
            if num in my_map:
                return True
            my_map[num] = my_map.get(num, 0) + 1
        return False
        
# In this solution we use a Hash Set to save every number in the array
# If it appears the first time, we store it in the Hash Set otherwise we have found a duplicate