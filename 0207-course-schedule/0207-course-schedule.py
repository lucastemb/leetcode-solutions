class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #idea: each pair represents neighbors in a graph 
        #each node will represent a class, with each neighbor being a prerequisite (yes)

        #create a map that lists the prerequistes (neighbors)
        preMap={i:[] for i in range(numCourses)} #create a map with an empty array for each number in the num of courses
        for crs, pre in prerequisites: #first value and second value
            preMap[crs].append(pre) #append pre to the array 
        visit=set()

        def dfs(crs):
            if crs in visit: #if the current course has already been visited return false
                return False
            if preMap[crs]==[]: #if the course has no prerequisites return true!
                return True
            visit.add(crs) #add courses to visited after the check has been completed
            for pre in preMap[crs]: #for the prerequisites in array check if they've been visited or if they have no prerequisites
                if not dfs(pre): return False #if the course has already been viisted that means something went wrong
            visit.remove(crs)
            preMap[crs] = [] #this is done to save time
            return True
        
        for crs in range(numCourses): #for every course run the dfs
            if not dfs(crs): return False #if the dfs returns false at any point return false
        return True

        #time: o(n*2^m)?
        #memory: o(n*2^m)






        