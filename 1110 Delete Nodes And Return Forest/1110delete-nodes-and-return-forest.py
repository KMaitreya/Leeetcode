# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)  # Convert list to set for O(1) lookups
        forest = []  # List to store the roots of the resulting trees

        def traverse(node, is_root):
            if not node:
                return None
            root_deleted = node.val in to_delete_set
            if is_root and not root_deleted:
                forest.append(node)
            node.left = traverse(node.left, root_deleted)
            node.right = traverse(node.right, root_deleted)
            return None if root_deleted else node

        traverse(root, True)
        return forest
