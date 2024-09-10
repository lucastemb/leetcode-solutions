# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, prefixSums, currSum):
            if not node: 
                return 0
            #add the current node to the running sum
            currSum+=node.val
            sums = 0
            #base case
            if currSum == targetSum: 
                sums+=1
            
            
            sums+=prefixSums.get(currSum-targetSum,0)
            prefixSums[currSum] = prefixSums.get(currSum,0)+1
            
            sums+=dfs(node.left, prefixSums, currSum)
            sums+=dfs(node.right, prefixSums, currSum)

            prefixSums[currSum] = prefixSums.get(currSum,1)-1
            return sums

        return dfs(root, {}, 0)

            