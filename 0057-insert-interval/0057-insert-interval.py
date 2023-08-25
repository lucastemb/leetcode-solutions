class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:] #return current intervals with newinterval appended at beginning
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) #add interval and continue 
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])] #create new interval
        res.append(newInterval)    
        return res


        #time: O(N)
        #space: O(N)