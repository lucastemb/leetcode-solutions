# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfs(node, string):
            nonlocal res
            string+=str(node.val)
            if not node.left and not node.right:
                res+=int(string)
            if node.left: 
                dfs(node.left, str(string))
            if node.right: 
                dfs(node.right, str(string))
        dfs(root, "")
        return res