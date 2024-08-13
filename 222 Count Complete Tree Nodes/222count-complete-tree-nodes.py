# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        cnt=0
        
        def traverse(node):
            nonlocal cnt
            if node:
                cnt+=1
                traverse(node.left)
                traverse(node.right)
            return

        traverse(root)

        return cnt