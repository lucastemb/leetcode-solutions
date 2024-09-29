class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles=sorted(piles)
        k = piles[-1]
        l, r = 1, piles[-1]

        while l < r:
            hours_needed=0
            m = (l+r)//2
            for num in piles: 
                hours_needed+=math.ceil(num/m)
            k = min(m, k)
            if hours_needed <= h:
                r=m
            else:
                l=m+1
        return l
            
            




