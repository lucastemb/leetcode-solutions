class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        for i in range(len(flowerbed)-1,-1,-1):
            if flowerbed[i] == 0:
                left_empty = (i==0) or (flowerbed[i-1] == 0)
                right_empty = (i==len(flowerbed)-1) or (flowerbed[i+1] == 0)
                if left_empty and right_empty:
                    flowerbed[i]=1
                    n-=1
        return n<=0