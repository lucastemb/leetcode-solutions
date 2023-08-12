class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #idea: each pair represents neighbors in a graph 
        #each node will represent a class, with each neighbor being a prerequisite (yes)

        #create a map that lists the prerequistes (neighbors)
        preMap={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit=set()

        def dfs(crs):
            if crs in visit: 
                return False
            if preMap[crs]==[]:
                return True
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

        







        