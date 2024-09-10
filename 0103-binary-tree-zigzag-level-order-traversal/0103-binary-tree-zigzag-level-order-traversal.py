# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q=deque()
        q.append(root)
        odd=True
        if not root: 
            return []
        while q:
            level=[]
            qLen=len(q)
            for i in range(qLen):
                curr=q.popleft()
                if curr:
                    level.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            if odd: 
                res.append(level)
            else:
                res.append(level[::-1])
            odd= not odd
        return res