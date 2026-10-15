from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter, w_size, match = Counter(s1), len(s1), 0

        for i in range(len(s2)):
            if s2[i] in counter:
                if not counter[s2[i]]: match -= 1
                counter[s2[i]] -= 1
                if not counter[s2[i]]: match += 1

            if i >= w_size and s2[i-w_size] in counter:
                if not counter[s2[i-w_size]]: match -= 1
                counter[s2[i-w_size]] += 1
                if not counter[s2[i-w_size]]: match += 1

            if match == len(counter):
                return True
        return False

# In this solution, we use a sliding window the size of s1 to see if a permutation of s1 is in s2
# We initialize a counter for s1 to check the frequency of characters we need to track
# When we iterate through s2, if the character is in the counter we check if the count for that character is 0
# If it is, we decrement because it means we are missing a character
# Then we decrement the count of that character in the counter. We check again if it's 0 because if it is, it means we have a match
# We do the same thing for the character leaving the window but increment the count instead
# If the match is equal to the length of unique characters it means there was a permutation