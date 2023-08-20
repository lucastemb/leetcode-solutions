class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])
        visit=set()
        count=0

        #idea: have the dfs function return true or false if it returns true increment the count by 1? 
        def dfs(r,c):
            if r not in range(ROWS) or c not in range(COLS):
                return 0
            if grid[r][c]==1 or (r,c) in visit: 
                return 1
            visit.add((r,c))
            #have them return something if any of them are True then we keep it going if the dfs
            #above 
            return min(dfs(r-1,c),
            #below
            dfs(r+1,c),
            #left
            dfs(r, c-1),
            #right
            dfs(r, c+1))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c]==0:
                    count+=dfs(r,c)
        return count

        #time: o(m*n*4^n)
        #space: ^ 