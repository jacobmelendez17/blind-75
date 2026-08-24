class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        left = max_length = 0
        for right in range(len(s)):
            freqs[s[right]] += 1
            maxFreq = max(freqs.values())
            currLen = right - left + 1
            if currLen - maxFreq > k:
                freqs[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
    
# In this approach we utilize a dynamic sliding window that checks the frequency of letters
# This frequency helps us find the favored char that we will change other chars to
# We use a dynamic approach to iterate through the string and update the values of a dictionary to track letter frequency
# We track our current length minus max frequency within the loop because if it's greater than k, we can't replace enough chars
# If that condition hits then we move our left pointer and decrease the frequency of that char