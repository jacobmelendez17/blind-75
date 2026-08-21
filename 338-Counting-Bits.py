class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for x in range(1, n + 1):
            ans.append(ans[x >> 1] + (x & 1))
        return ans

# In this solution we use dynamic programming to find the 1's in the binary of integers
# ans[x >> 1] will give us the number of 1's in an integer because it's the same as x // 2
# (x & 1) will give us the last bit since we did the right shift