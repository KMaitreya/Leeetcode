# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def helper(sub, node):
            if not sub and not node: return True
            if sub and node and sub.val==node.val:
                return helper(sub.left, node.left) and helper(sub.right, node.right)
            return False


        if not subRoot: return True
        if not root: return False

        if helper(subRoot, root):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

       