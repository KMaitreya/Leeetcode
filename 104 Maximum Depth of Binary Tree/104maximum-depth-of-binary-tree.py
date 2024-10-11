# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ### Recursive DFS

        # if root:
        #     return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
        # return 0


        ### BFS

        if root:

            q=[root]
            level=0

            while True:
                for i in range(len(q)):
                    node=q.pop(0)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                level+=1

                if len(q)==0:
                    break

            return level

        return 0