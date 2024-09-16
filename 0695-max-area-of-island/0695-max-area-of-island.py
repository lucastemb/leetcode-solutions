class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        max_area=0

        def dfs(r,c):
            if (r,c) in visited or r not in range(len(grid)) or c not in range(len(grid[0])) or grid[r][c] == 0:
                return 0
            visited.add((r,c))
            return 1+dfs(r,c+1)+dfs(r,c-1)+dfs(r+1,c)+dfs(r-1,c)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area=max(dfs(r,c), max_area)
        return max_area
