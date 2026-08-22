class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or mapping[char] != stack.pop():
                    return False
        return not stack

# In this solution, we save all our possible brackets into a dictionary
# We iterate throught the string and if the char matches a value, it is an opening bracket
# Opening brackets will be stored in the stack
# If the char matches a key, it is a closing bracket
# If the char is not a key in the map or is a key but doesn't have a corresponding bracket in the stack it is not valid
# If the stack ends up empty it means all the brackets are valid