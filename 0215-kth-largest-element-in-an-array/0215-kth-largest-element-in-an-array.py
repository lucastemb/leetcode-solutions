class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        kth_element=0
        for num in nums:
            heapq.heappush(h, -1*num)
        for i in range(k):
            kth_element=-1*heapq.heappop(h)
        return kth_element
        #return(heapq.nlargest(k, h)[-1])
        #time: O(nlog(n))
        #space: O(n)