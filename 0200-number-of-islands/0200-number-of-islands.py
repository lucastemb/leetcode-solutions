class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0: 
            return 0
        ROWS=len(grid)
        COLS=len(grid[0])
        visit=set()
        islands=0
        
        def dfs(r,c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c]=='0' or (r,c) in visit: 
                return
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1" and (r,c) not in visit:
                    islands+=1
                    dfs(r,c)

        return islands