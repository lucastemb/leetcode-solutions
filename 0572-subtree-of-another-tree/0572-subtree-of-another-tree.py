# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node is None: 
                return False
            elif is_identical(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        def is_identical(f,s):
            if f is None or s is None: 
                return f is None and s is None
            return (f.val==s.val and is_identical(f.left, s.left) and is_identical(f.right, s.right))
        
        return dfs(root)

