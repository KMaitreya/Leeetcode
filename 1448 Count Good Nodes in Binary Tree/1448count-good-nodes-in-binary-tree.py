# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, val):
            if node:
                res=1 if node.val>=val else 0
                val=max(node.val, val)
                return dfs(node.left, val)+dfs(node.right, val)+res
            return 0

        
        return dfs(root, root.val)