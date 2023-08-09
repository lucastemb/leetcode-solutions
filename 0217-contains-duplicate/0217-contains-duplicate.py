class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for c in nums: 
            if c in d:
                return True
            d[c]=1
        return False    
            
 