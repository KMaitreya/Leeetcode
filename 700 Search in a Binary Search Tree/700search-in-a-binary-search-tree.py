# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # nnode=None
        
        # def traverse(node):
        #     nonlocal nnode
        #     if node:
        #         if node.val==val:
        #             nnode=node
        #             return
        #         traverse(node.left)
        #         traverse(node.right)
        #     return node

        # traverse(root)
        # return nnode

        while root:
            if root.val==val:
                return root
            elif root.val>val:
                root=root.left
            else:
                root=root.right

