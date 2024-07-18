# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return defaultdict(int)
            
            if not node.left and not node.right:
                return defaultdict(int, {1: 1})
            
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Count good leaf pairs
            for ld in left_distances:
                for rd in right_distances:
                    if ld + rd <= distance:
                        self.count += left_distances[ld] * right_distances[rd]
            
            # Collect current node's distances
            current_distances = defaultdict(int)
            for d in left_distances:
                if d + 1 <= distance:
                    current_distances[d + 1] += left_distances[d]
            for d in right_distances:
                if d + 1 <= distance:
                    current_distances[d + 1] += right_distances[d]
            
            return current_distances
        
        self.count = 0
        dfs(root)
        return self.count