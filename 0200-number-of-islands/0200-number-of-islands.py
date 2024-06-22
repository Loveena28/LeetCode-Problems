class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        countIslands = 0
        
        def dfs(i,j):
            grid[i][j] = '0'
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            for dx,dy in directions:
                nx,ny = dx + i,dy + j
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == '1':
                    dfs(nx,ny)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    dfs(i,j)
                    countIslands = countIslands + 1
        return countIslands