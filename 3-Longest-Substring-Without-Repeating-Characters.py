class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length = 0
        char_set = set()
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

# In this solution we use a dynamic sliding window to find the longest substring
# If the current character of the right pointer is unique we add it to the set
# We continue moving the right pointer and keeping the left while characters are unique
# If there is a repeat character in the set we remove the old one which is the char left is curently pointing to
# We add right's char regardless and continue through while getting the max length
# The longest length is checked by getting the size of the window (right-left) and adding 1 since the array index is offset by 1