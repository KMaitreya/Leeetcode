# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        arr=[]
        cnt=0
        q=[]
        q.append(root)
        while q:
            level=0
            for _ in range(len(q)):
                node=q.pop(0)
                level+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            heapq.heappush(arr, -level)
            cnt+=1

        if k>cnt:
            return -1

        heapq.heapify(arr)

        for _ in range(1, k):
            heapq.heappop(arr)

        return -heapq.heappop(arr)




            