class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], []
        for word in strs:
            sizes.append(len(word))
        for size in sizes:
            res.append(str(size))
            res.append(',')
        res.append('#')
        res.extend(strs)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res = [], []
        i = 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1 # skip ','
        i += 1 # skip '#'
        for size in sizes:
            res.append(s[i:i + size])
            i += size
        return res

# In this solution, we need to encode a list of strings by making it one string so we will organize it to be readable
# We first get the sizes of each string and separate them by commas in a list
# We then separate the actual words after that with a '#' and the words after as one long string
# To decode it, we parse our string by converting the list of sizes into integers and storing them in a list
# Once we hit our indicator (#) we use the array of sizes to extract word lengths from the long word string and return that as a list