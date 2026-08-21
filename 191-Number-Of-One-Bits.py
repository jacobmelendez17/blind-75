class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        while n != 0:
            if(n & 1 == 1):
                bits += 1
            n >>= 1
        return bits

# In this solution we look at the bit value of n and just read through that
# We start leftmost and simply see if the bit of n is 1 or 0 and then shift to the next bit on the right
# This one only requires bit manipulation