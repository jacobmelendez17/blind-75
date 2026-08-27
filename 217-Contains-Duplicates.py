class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        
# In this solution we use a set to save every number in the array
# If it appears the first time, we store it in the set otherwise we have found a duplicate