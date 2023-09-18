class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #if the current number is less than the target move left
        #if the current number is greater than the target move right
        i=0
        visited=set()
        while i in range(len(nums)):
            print(i)
            if nums[i]==target:
                return i
            if nums[i] < target: 
                if i == len(nums)-1: 
                    i=0
                else:
                    i+=1
            if nums[i] > target:
                if i == 0:
                    i=len(nums)-1
                else:
                    i-=1
            if i in visited:
                break
            visited.add(i)
        return -1
            
        
        