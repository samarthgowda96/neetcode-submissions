# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = 0
        def dfs(root):
            nonlocal count
            if not root:
                return


            
            res = dfs(root.left)
            if res is not None:
                return res
            count+=1
            if count == k:
                return root.val
            res = dfs(root.right)
            if res is not None:
                return res

            
        return dfs(root)
        