# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        pre=[]
        
        def traversal(node):
            if node:
                pre.append(node.val)
                traversal(node.left)
                traversal(node.right)
            else: 
                return 

        traversal(root)

        return pre