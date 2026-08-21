class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
        
# In this solution, we use a two-pointer that starts at the ends and works towards the middle
# If the characters are not alphanumeric (isalnum), we skip and move the pointer
# If the character are then we check if they are equal and move on