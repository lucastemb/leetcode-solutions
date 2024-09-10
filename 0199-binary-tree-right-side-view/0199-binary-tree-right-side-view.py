# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        q=deque()
        q.append(root)
        res=[]
        while q:
            level=[] 
            qLen=len(q)
            for i in range(qLen):
                curr=q.popleft()
                if curr:
                    level.append(curr)
                    if curr.left: 
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            res.append(level[-1].val)
        return res
