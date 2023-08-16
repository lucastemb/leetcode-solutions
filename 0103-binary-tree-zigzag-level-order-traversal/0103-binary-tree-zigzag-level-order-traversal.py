# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=deque()
        q.append(root)
        res=[]
        count=0
        while q:
            qLen=len(q)
            currentLevel=[]
            for i in range(qLen):
                node=q.popleft()
                currentLevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if count % 2 == 0:
                res.append(currentLevel)
            else:
                res.append(currentLevel[::-1])
            count+=1
            
        return res
