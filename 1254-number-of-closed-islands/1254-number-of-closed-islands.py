class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        res=0
        def dfs(r,c):
            if r not in range(len(grid)) or c not in range(len(grid[0])):
                return 0
            if grid[r][c] == 1 or (r,c) in visited: 
                return 1
            
            visited.add((r,c))
            return min(dfs(r,c+1),
            dfs(r, c-1),
            dfs(r+1, c),
            dfs(r-1, c))
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == 0:
                    res+=dfs(r,c)
        return res