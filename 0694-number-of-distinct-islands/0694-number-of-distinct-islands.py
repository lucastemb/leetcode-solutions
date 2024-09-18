class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands=set()
        visited=set()
        def dfs(r,c, direction):
            if (r,c) in visited or r not in range(len(grid)) or c not in range(len(grid[0])) or grid[r][c] == 0: 
                return
            visited.add((r,c))
            path_signature.append(direction)
            dfs(r+1,c,"D")
            dfs(r-1,c,"U")
            dfs(r,c+1,"R")
            dfs(r,c-1,"L")
            path_signature.append("0")
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    path_signature = []
                    dfs(r,c,"0")
                    islands.add(tuple(path_signature))     
        return len(islands)
        