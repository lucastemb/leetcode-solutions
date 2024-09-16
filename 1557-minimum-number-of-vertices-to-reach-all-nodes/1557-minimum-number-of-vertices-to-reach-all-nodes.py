class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        #create adjacency list 
        adj_list = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for u,v in edges:
            adj_list[u].append(v) #it's directed
            indegrees[v]+=1
        #create dfs
        def dfs(node, visited):
            if node not in visited:
                visited.add(node)
                for edge in adj_list[node]:
                    dfs(edge, visited)

        #start creating the array
        visited=set()
        res=[] #resulting array
        for vertex in list(adj_list):
            if vertex not in visited:
                if indegrees[vertex] == 0:
                    res.append(vertex)
                dfs(vertex, visited)
                visited.add(vertex)
        return res


