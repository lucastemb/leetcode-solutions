class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals, key=lambda x: x[0])
        res=[]
        for start, end in intervals:
            if len(res)==0 or res[-1][1] < start:
                res.append([start,end])
            if res[-1][1] >= start:
                res[-1]=[res[-1][0], max(res[-1][1], end)]
        return res
            
            