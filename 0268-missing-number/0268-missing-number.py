class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #inefficient solution
        res={}
        maxNum=0
        for num in nums:
            res[num]= 1+res.get(num,0)
            maxNum=max(maxNum, num)
        for i in range(maxNum+1):
            if i not in res: 
                return i
        return i+1