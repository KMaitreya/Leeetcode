# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ## METHOD 1

        res=[]

        def traverse(node):
            nonlocal res
            if node:
                traverse(node.left)
                res.append(node.val)
                traverse(node.right)
            return

        traverse(root)

        cnt=res[k-1]
        del res

        return cnt

