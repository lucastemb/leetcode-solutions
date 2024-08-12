class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res=0
        s=sorted(nums)
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l < r:
                smaller = s[l] + s[i] + s[r]
                if smaller < target:
                    res+=r-l
                    l+=1
                else: 
                    r-=1
        return res