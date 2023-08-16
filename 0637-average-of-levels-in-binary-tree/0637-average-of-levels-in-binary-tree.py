# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=deque()
        res=[]
        q.append(root)

        while q:
            qLen=len(q)
            levelSum=0
            for i in range(qLen):
                node=q.popleft()
                levelSum+=node.val
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            res.append(float(levelSum)/qLen)
        return res
            