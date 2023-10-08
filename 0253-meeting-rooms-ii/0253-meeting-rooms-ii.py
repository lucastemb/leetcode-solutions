class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        if they overlap, then you can increment the count by 1
        use heap if the min heap value is less than the start time of a meeting in the sorted array pop the min put the new one in 
        '''

        h=[]
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(h, intervals[0][1])
        for i in range(1, len(intervals)):
            if h[0] <= intervals[i][0]:
                heapq.heappop(h)
            heapq.heappush(h, intervals[i][1])
        return len(h)

        
        
        
        