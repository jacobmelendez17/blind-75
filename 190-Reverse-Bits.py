class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res

# In this solution we use bit manipulation to set the rightmost bit to the leftmost bit of the result
# We extract the rightmost bit of n then shift the result to the left and add the extracted bit to the result
# We shift n back to the right to get the next bit