"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        res=[]
        q=deque()
        q.append(root)
        if not root:
            return root
        while q: 
            qLen=len(q)
            level=[]
            for i in range(qLen):
                curr=q.popleft()
                if curr:
                    level.append(curr)
                    if curr.left: 
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            #for every item in level connect them to next
            for j in range(qLen-1, -1, -1):
                if j == qLen-1: 
                    level[j].next=None
                else: 
                    level[j].next=level[j+1]
        return root
                    