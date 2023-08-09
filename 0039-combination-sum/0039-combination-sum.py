class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #backtracking requires dfs

        #array that stores results
        
        #i know i have to use dfs, but i don't know how to get each permutation

        res=[]
        #need a dfs function to search all possible combinations in array
        def dfs(index, curr, total):
            if total == target: 
                res.append(curr.copy())
                return
            if index >= len(candidates) or total > target: 
                return 

            curr.append(candidates[index])
            dfs(index, curr, total+candidates[index])
            curr.pop()
            dfs(index+1, curr, total)
        dfs(0, [], 0)
        return res


