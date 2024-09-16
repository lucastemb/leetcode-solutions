class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        #create adjacency list 
        indegrees = collections.defaultdict(int)
        for u,v in edges:
            indegrees[v]+=1

        #start creating the array
        res=[] #resulting array
        for i in range(n):
            if indegrees[i] < 1:
                res.append(i)
        return res


