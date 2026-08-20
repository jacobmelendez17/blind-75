# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxLeft = self.maxDepth(root.left)
        maxRight = self.maxDepth(root.right)
        return max(maxLeft, maxRight) + 1

# In this recursive solution, our integers maxLeft and maxRight are set based on how many times they are called
# This also covers the case if there is only a root node so regardless of the iterations, a 1 is always added to account for the root