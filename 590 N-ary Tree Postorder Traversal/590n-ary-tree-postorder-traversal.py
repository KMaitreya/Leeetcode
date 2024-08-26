"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        op=[]
        
        def traverse(node):
            if node:
                for child in node.children:
                    traverse(child)
                op.append(node.val)
            return

        traverse(root)

        return op