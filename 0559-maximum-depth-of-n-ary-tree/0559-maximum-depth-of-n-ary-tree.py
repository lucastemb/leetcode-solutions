"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        q=deque()
        q.append(root)
        if not root:
            return 0
        length=0
        while q: 
            qLen = len(q)
            length+=1
            for i in range(qLen):
                curr = q.popleft()
                if curr.children: 
                    for j in range(len(curr.children)):
                        q.append(curr.children[j])
        return length
            


        
