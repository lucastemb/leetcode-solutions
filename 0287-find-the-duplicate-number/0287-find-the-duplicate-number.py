class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numlist={}
        for i in nums: 
            numlist[i]=1+numlist.get(i,0)
            if numlist[i] > 1: 
                return i
        return -1