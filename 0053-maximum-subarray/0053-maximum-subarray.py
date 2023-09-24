class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=nums[0] #init maxSub arr to first number
        currSum=0 
        for n in nums: 
            if currSum < 0: #if the currSum is less than zero discard it (what does it matter?))
                currSum = 0 #set it equal to zero
            currSum += n #add n to the currSum
            maxSub=max(maxSub, currSum) #maxSub array = currMax sub arr or currSum
        return maxSub