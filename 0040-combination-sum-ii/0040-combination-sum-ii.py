class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        backtracking: 
                (.)
                /  \
              (1)     (.)
            /    \    /    \
          (1,2)     (2)     (.)
          
        solution (1): 
        dfs() time: o(n*2^n) space: o(n)
        '''
        candidates.sort()
        res=[]
        def dfs(curr, pos, target):
          if target==0:
            res.append(curr.copy())
            return
          if target <= 0:
            return 
          prev = -1
          for i in range(pos, len(candidates)):
            if candidates[i] == prev:
              continue
            curr.append(candidates[i])
            dfs(curr, i+1, target-candidates[i])
            curr.pop()
            prev=candidates[i]
        dfs([],0,target)
        return res
