class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #going to need to a bfs(?)
        if not grid: 
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        islands=0

        def bfs(r,c):
            q=deque()
            visited.add((r,c))
            q.append((r,c))

            while q: 
                row, col = q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]

                for v, h in directions: 
                    r,c = row+v, col+h
                    if (r in range(ROWS) and c in range(COLS) and grid[r][c] == "1" and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands


        #time complexity will be O(m*n*4^n) again? 
