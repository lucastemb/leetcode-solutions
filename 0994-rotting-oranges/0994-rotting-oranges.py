class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        q=deque()
        time, fresh = 0,0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2: 
                    q.append((r,c))

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while q and fresh > 0:
            qLen=len(q)
            for i in range(qLen):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    #if in bounds and fresh, make rotten
                    if row not in range(len(grid)) or col not in range(len(grid[0])) or grid[row][col] != 1:
                        continue
                    grid[row][col]=2
                    q.append([row,col])
                    fresh -= 1
            time+=1 
        return time if fresh == 0 else -1
        