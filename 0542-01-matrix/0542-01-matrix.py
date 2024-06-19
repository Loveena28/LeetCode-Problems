from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows,cols = len(mat),len(mat[0])
        ans = [[-1] * cols for _ in range(rows)]
        
        queue = deque()
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    queue.append((i,j))
        
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        
        while queue:
            x,y = queue.popleft()
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<rows and 0<=ny<cols and ans[nx][ny] == -1:
                    ans[nx][ny] = ans[x][y] + 1
                    queue.append((nx,ny))
        
        return ans
            