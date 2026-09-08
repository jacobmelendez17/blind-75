class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# In this solution, we use a hash map and 2D frequency array to track the frequency of numbers with a bucket sort
# We create arrays within our array freq and add +1 in case the highest frequency is equal to the length of the array
# Then, we add each number to the hash map and increment the counter of how often it appears
# We move all our numbers into the frequency array based on how often they occur
# Finally, we iterate through the array backwards and add our highest frequent numbers until it reaches k
# The idea behind this is that each index of the frequency array represent how many times a number appears
# If the number '2' appears 3 times, we move '2' into the third index
# Now when we iterate backwards, we are starting at the index that represents the highest frequency