class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        for num in nums: 
            heapq.heappush(h, 1*num)
        return heapq.nlargest(k,h)[-1]

        