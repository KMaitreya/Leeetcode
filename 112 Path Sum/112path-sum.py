# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False
        
        def backtrack(s, node):
            if not node.right and not node.left:
                return s==targetSum
            
            return (backtrack(s+node.left.val, node.left) if node.left else False) or (backtrack(s+node.right.val, node.right) if node.right else False)

            
        return backtrack(root.val, root)