class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())

# In this solution we use a hashmap to organize sorted keys with corresponding words
# For every word, we sort it and store it as a value for its corresponding matching key
# At the end we convert the map to a list of the values to return