class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        for num in nums:
            heapq.heappush(h, num)
        return(heapq.nlargest(k, h)[-1])
            