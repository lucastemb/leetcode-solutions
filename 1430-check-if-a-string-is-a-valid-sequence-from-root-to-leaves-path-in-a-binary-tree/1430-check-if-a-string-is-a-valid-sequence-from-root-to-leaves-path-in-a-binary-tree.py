# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        def dfs(node, path):
            if not node: 
                return False
            path.append(node.val)
            if path == arr and (not node.left and not node.right):
                print("found it!")
                return True
            return (dfs(node.left, list(path)) or dfs(node.right, list(path)))
        return dfs(root, [])
