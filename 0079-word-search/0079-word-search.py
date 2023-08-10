class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #backtracking so you need to do dfs()

        ROWS = len(board)
        COLS = len(board[0])

        visited=set()
        #you keep track is the r and c has been visited or not
        def dfs(r,c, curr):
            if curr == len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or word[curr] != board[r][c] or (r,c) in visited:
                return False
            visited.add((r,c))
            res = (
            #below 
            dfs(r+1,c, curr+1) or
            #above
            dfs(r-1,c, curr+1) or
            #left
            dfs(r,c-1, curr+1) or
            #right
            dfs(r,c+1, curr+1)
            )
            visited.remove((r,c))
            return res
        

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): return True
        return False

        #time: O(m*n*4^n)
        #memory: O(m*n*4^n)