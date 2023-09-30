class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        solution: backtracking 
        dfs
        time: o(n*3^n) space:o(n)

                      (.)
                    /    \
                (2)        (.)
                /  \       /  \
            (2,3)   (2,6) (3)  (.)
            .....

        '''

        res=[]
        subset=[] #arr contain the subsets that may equal to the target
        def dfs(i):
            if sum(subset) == target and subset not in res: #equals to target
                res.append(subset.copy())
            if i >= len(candidates) or sum(subset) > target: #out of bounds
                return
            subset.append(candidates[i])
            dfs(i)
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res


        


