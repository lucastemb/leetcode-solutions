class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return 

        ROWS, COLS = len(rooms), len(rooms[0])
        queue = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r,c))

        while queue:
            row, col = queue.popleft()
            print(row,col)
            for dx, dy in ([0,1], [0,-1], [1,0], [-1,0]):
                new_row, new_col = row+dx, col+dy
                if new_row in range(ROWS) and new_col in range(COLS) and rooms[new_row][new_col] == 2147483647:
                    rooms[new_row][new_col] = rooms[row][col] +1
                    queue.append((new_row, new_col))
        return rooms

