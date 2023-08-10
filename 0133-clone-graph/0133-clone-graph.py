"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #do dfs 
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val) #head/ starting point
            oldToNew[node]=copy
            for neighbor in node.neighbors: 
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node) if node else None
