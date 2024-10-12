# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def construct(inorder):
            if inorder:
                val=preorder.pop(0)
                i=inorder.index(val)
                node=TreeNode(val)
                node.left=construct(inorder[:i])
                node.right=construct(inorder[i+1:])
                return node
            return

        return construct(inorder)
