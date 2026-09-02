# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                return 0

            if root.left is None and root.right is None:
                return depth
            

            left = dfs(root.left, 1+depth)
            right = dfs(root.right, 1+depth)

            return max(left, right)
        return dfs(root, 1)


        