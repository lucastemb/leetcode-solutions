# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        allPaths=[]
        if not root:
            return []
        def dfs(node, curr_sum, path):
            curr_sum += node.val
            path.append(node.val)
            if (not node.left and not node.right) and curr_sum == targetSum: 
                allPaths.append(list(path))
            if node.left:
                left = dfs(node.left, curr_sum, list(path))
            if node.right: 
                right = dfs(node.right,curr_sum, list(path))
        dfs(root,0,[])
        return allPaths