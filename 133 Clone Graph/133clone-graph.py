"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        hmap={}

        def dfs(node):
            if node in hmap:
                return hmap[node]
            cpy=Node(node.val)
            hmap[node]=cpy
            for n in node.neighbors:
                cpy.neighbors.append(dfs(n))
            return cpy

        if node:
            return dfs(node)
        return None

            
        
                 

      