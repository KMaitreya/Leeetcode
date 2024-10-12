# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        #### DFS solution
        
        # res=[]
        
        # def rheight(node):
        #     nonlocal res
        #     if node:
        #         res.append(node.val)
        #         return rheight(node.right)+1
        #     return 0
        
        # def dfs(node, height, r):
        #     nonlocal res
        #     if node:
        #         if height>r:
        #             res.append(node.val)
        #         dfs(node.left, height+1, r)
        #         dfs(node.right, height+1, r)
        #     return 
        
        # r=rheight(root)
        # dfs(root, 0, r-1)

        # print(r)

        # return res



        ### BFS solution

        q=[root]
        res=[]
        rlevel=0

        while True:
            for i in range(len(q)):
                t=q.pop(0)
                if t:
                    rlevel=t.val
                    q.append(t.left)
                    q.append(t.right)
            
            if not q:
                break
            
            res.append(rlevel)

        return res
            
