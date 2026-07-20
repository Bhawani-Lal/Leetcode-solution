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
        # Empty graph
        if node is None:
            return None

        # Stores original node and its cloned node
        cloned_nodes = {}

        def dfs(current_node):

            # If already cloned, return its clone
            if current_node in cloned_nodes:
                return cloned_nodes[current_node]

            # Create a new copy of current node
            copy_node = Node(current_node.val)

            # Save it before visiting neighbours
            cloned_nodes[current_node] = copy_node

            # Clone every neighbour
            for neighbour in current_node.neighbors:
                cloned_neighbour = dfs(neighbour)
                copy_node.neighbors.append(cloned_neighbour)

            return copy_node

        return dfs(node)
