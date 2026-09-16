class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        pre = suf = 1
        for i in range(n):
            res[i] = pre
            pre *= nums[i]
        for i in range(n - 1, -1, -1):
            res[i] *= suf
            suf *= nums[i]

        return res

# In this solution we find the prefix and suffix of each element and then multiply them to get our answer
# We could create an array for prefex and suffix separately then multiply but this is more space efficient by applying suffix product directly to prefix
# We first get the prefix by starting at 1 and multiplying the next element by our pre variable and continuing that way
# We then traverse the array backwards, multiply our element in res by the current suffix, then add on to the suffix for the next iteration