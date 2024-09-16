class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces=len(isConnected)
        adj_list=defaultdict(list)
        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if isConnected[r][c] == 1 and r != c:
                    adj_list[r].append(c)

        def dfs(node, visited):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
        
        visited=set()
        res=0
        for city in range(provinces):
            if city not in visited:
                dfs(city, visited)
                res+=1
                
        return res