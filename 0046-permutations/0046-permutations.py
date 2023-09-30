class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        #space: o(n) 
        #time: o(n!)
        all of anything == dfs backtracking approach
                (.)
               /    \




        if nums[1,2,4]
        '''
        res=[] #result array
        if (len(nums)==1): #if len(nums==1)
            return [nums[:]] #return just the number itself
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            print("perms:",perms)
            
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            print('res:', res)
            nums.append(n)
        return res