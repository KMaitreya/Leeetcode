# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        q=[root]
        j=0

        while q:
            n=len(q)
            if j%2!=0:
                l=0
                r=n-1
                while l<r:
                    q[l].val, q[r].val=q[r].val, q[l].val
                    l+=1
                    r-=1
            for i in range(n):
                node=q.pop(0)
                if node.left and node.right:
                    q.append(node.left)
                    q.append(node.right)
            j+=1


        return root

                    