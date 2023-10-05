class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count=0
        ROWS=len(board)
        COLS=len(board[0])
        visited=set()
        def dfs(r,c):
            if (r,c) in visited or r not in range(ROWS) or c not in range(COLS) or board[r][c]=='.':
                return
            visited.add((r,c))
            #move down
            dfs(r+1,c)
            #move up
            dfs(r-1,c)
            #move right
            dfs(r,c+1)
            #move left
            dfs(r,c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'X' and (r,c) not in visited:
                    dfs(r,c)
                    count+=1
        return count