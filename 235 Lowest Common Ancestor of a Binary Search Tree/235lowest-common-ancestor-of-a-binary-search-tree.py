# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        
        def traverse(node):
            if node:
                if p.val<node.val and q.val>node.val or p.val>node.val and q.val<node.val or p.val==node.val or q.val==node.val:
                    return node
                return traverse(node.left) or traverse(node.right)

        return traverse(root)
