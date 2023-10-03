# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=deque()
        q.append(root)
        if not root:
            return []
        while q: 
            qLen=len(q)
            maxVal=float("-inf")
            for i in range(qLen):
                curr=q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                maxVal=max(maxVal, curr.val)
            res.append(maxVal)
        return res    

        