class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            count=0
            while i: 
                count+=i%2
                i=i>>1
            ans.append(count)
        return ans

                 

