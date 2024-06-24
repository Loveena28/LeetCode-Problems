from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque([(0,0,1)]) # row,column,length
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        directions = [(-1,0),(0,-1),(1,0),(0,1),(1,1),(-1,-1),(1,-1),(-1,1)]
        
        visited = set((0,0))
        
        while queue:
            r,c,length = queue.popleft()
            if (min(r,c) < 0 or max(r,c) >= n) or grid[r][c]:
                continue
            if r == n - 1 and c == n - 1:
                return length
            for dx,dy in directions:
                nx,ny = r+dx,c+dy
                if (nx,ny) not in visited:
                    visited.add((nx,ny))
                    queue.append((nx,ny,length+1))
        
        return -1