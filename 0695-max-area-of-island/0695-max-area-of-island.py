class Solution:
    def maxAreaOfIsland(self, matrix: List[List[int]]) -> int:
        biggestIslandArea = 0
        ROWS=len(matrix)
        COLS=len(matrix[0])
        visit=set()

        def dfs(r,c):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visit:
                return 0
            if matrix[r][c]==0:
                return 0
            visit.add((r,c))
            add=1
            #up
            add+=dfs(r-1,c)
            #down
            add+=dfs(r+1,c)
            #right
            add+=dfs(r,c+1)
            #left
            add+=dfs(r,c-1)
            return add

        for r in range(ROWS):
            for c in range(COLS):
                if (matrix[r][c]==1 and (r,c) not in visit):
                    biggestIslandArea=max(dfs(r,c),biggestIslandArea)
        return biggestIslandArea