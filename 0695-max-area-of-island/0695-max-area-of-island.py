class Solution:
    def maxAreaOfIsland(self, matrix: List[List[int]]) -> int:
        biggestIslandArea=0
        ROWS=len(matrix)
        COLS=len(matrix[0])
        visited=set()

        def dfs(r,c):
            if (r,c) in visited or r not in range(ROWS) or c not in range(COLS) or matrix[r][c]==0:
                return 0
            visited.add((r,c))
            return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1))
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 1 and (r,c) not in visited:
                    biggestIslandArea=max(dfs(r,c),biggestIslandArea)
        return biggestIslandArea