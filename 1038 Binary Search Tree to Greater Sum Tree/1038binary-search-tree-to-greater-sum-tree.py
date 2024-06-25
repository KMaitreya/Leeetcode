# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        self.sum = 0  # Initialize the running sum
        
        def reverse_in_order(node: TreeNode):
            if not node:
                return
            
            # Traverse the right subtree first
            reverse_in_order(node.right)
            
            # Update the running sum and the node's value
            self.sum += node.val
            node.val = self.sum
            
            # Traverse the left subtree
            reverse_in_order(node.left)
        
        # Start the reverse in-order traversal from the root
        reverse_in_order(root)
        
        return root