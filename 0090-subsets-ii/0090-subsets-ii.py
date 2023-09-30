class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        bc you have to find all possible permutations: do backtracking :)
            (.)
           /    \
        (1)     (.)
        /   \     /  \
       (1,2)  (1)      (2)  (.)

       [1,2,2]
       []
       [1]
       [1,2]
       [1,2,2]
       [2]
       [2,2]
        '''
        res=[]
        subset=[]
        def dfs(i):
            if i >= len(nums):
                if sorted(subset) not in res:
                    res.append(sorted(subset.copy()))
                return
            
            #if we take it
            subset.append(nums[i])
            dfs(i+1)

            #don't take it
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

        #space: o(n)
        #time: o(n*2^n)