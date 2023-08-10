class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #going to need to a bfs(?)

        #if the grid doesn't exist, return 0 islands
        if not grid: 
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        islands=0

        #call bfs bc you can start from the first zero and then branch out
        def bfs(r,c): #this was done iteratively 
            q=deque() #to properly implement a bfs you need to call a queue
            visited.add((r,c)) #add the root (the first element you landed on)
            q.append((r,c)) #add the r and c to the queue

            while q: #while there are still items in the queue
                row, col = q.popleft() #remove tuple with row and col from queue
                directions=[[1,0],[-1,0],[0,1],[0,-1]] #down, up, right, left

                for v, h in directions: #for vertical and horizontal offset in directions
                    r,c = row+v, col+h #apply vertical offest to row and horizontal offset to cols
                    if (r in range(ROWS) and c in range(COLS) and grid[r][c] == "1" and (r,c) not in visited): #if r is still in range, c is still in range, the tile at [r][c] is equal to 1, and the tile has not been visited before
                        q.append((r,c))
                        visited.add((r,c))

        for r in range(ROWS): 
            for c in range(COLS): #for every item perform a bfs 
                if grid[r][c] == "1" and (r,c) not in visited: #this line is to avoid duplicates
                    bfs(r,c) #call the bfs
                    islands+=1 #at the end of the call increment island count
        return islands


        #time complexity will be O(m*n*4^n) again? 
