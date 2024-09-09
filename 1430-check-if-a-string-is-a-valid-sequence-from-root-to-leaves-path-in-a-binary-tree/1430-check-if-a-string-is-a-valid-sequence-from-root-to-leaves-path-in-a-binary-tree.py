# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        def dfs(node, index):
            if not node: 
                return False
            seqLen = len(arr)
            if index >= seqLen or arr[index] != node.val:
                return False
            if index == seqLen-1 and (not node.left and not node.right):
                return True
            return (dfs(node.left, index+1) or dfs(node.right, index+1))
        return dfs(root, 0)
