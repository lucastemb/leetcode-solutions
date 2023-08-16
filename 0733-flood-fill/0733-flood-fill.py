class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS=len(image)
        COLS=len(image[0])
        visit=set()
        prev=image[sr][sc]

        def dfs(r,c):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visit or image[r][c] != prev:
                print(image[sr][sc])
                return
            image[r][c]=color
            visit.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        dfs(sr,sc)

        return image