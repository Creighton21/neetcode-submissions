"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: # Null case
            return None

        stack = [node] # frontier
        copy = {node: Node(node.val)} # discovery
        
        while stack:
            original = stack.pop()

            for neighbor in original.neighbors: 
                if neighbor not in copy: # Don't re-discover or create seen nodes.
                    copy[neighbor] = Node(neighbor.val) # Discover
                    stack.append(neighbor) # Push to the stack

                copy[original].neighbors.append(copy[neighbor]) # Add the neighbor

        return copy[node]