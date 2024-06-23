class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        maxArea = 0
        
        def dfs(i,j):
            grid[i][j] = 0
            directions = [(-1,0),(0,-1),(1,0),(0,1)]
            localArea = 1
            for dx,dy in directions:
                nx,ny = i+dx,j+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == 1:
                    localArea = localArea + dfs(nx,ny)
            return localArea
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxArea = max(maxArea,dfs(i,j))
        return maxArea