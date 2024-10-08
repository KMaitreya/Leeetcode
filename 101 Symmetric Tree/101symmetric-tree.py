# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        
        def traverse(lnode, rnode):
            if not lnode and not rnode: return True
            if not lnode or not rnode: return False
            return lnode.val==rnode.val and traverse(lnode.left, rnode.right) and traverse(lnode.right, rnode.left)
        
        return traverse(root.left, root.right)

        