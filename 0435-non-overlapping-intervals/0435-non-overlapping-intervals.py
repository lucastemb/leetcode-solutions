class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count=0
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        res=[intervals[0]]
        for start, end in intervals[1:]:
            lastEnd=res[-1][1]
            if start < lastEnd: 
                count+=1
            else: 
                res.append([start, end])
        return count