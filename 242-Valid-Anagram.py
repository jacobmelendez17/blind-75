class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = [0] * 26
        for x in range(len(s)):
            freq[ord(s[x]) - ord('a')] += 1
            freq[ord(t[x]) - ord('a')] -= 1
        
        for x in range(len(freq)):
            if freq[x] != 0:
                return False
        return True


# In this solution, we will use a frequency array to keep track of character counts in each word
# ord will provide the ASCII value and if both words contain that letter, it'll eventually zero out
# We check for zeros in the second for-loop and if everything isn't zero then there isn't an anagram