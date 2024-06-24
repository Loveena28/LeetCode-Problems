import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols = len(heights),len(heights[0])
        minHeap = [(0,0,0)] # diff,row,col
        visited = set((0,0))
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        while minHeap:
            diff,x,y = heapq.heappop(minHeap)
            
            if (x,y) in visited:
                continue
             
            visited.add((x,y))
            
            if x==rows-1 and y==cols-1:
                return diff
            
            for dx,dy in directions:
                nx,ny = dx+x,dy+y
                
                if 0 > nx or 0 > ny or nx >= rows or ny >= cols or (nx,ny) in visited:
                    continue
                
                newDiff = max(diff,abs(heights[x][y]-heights[nx][ny]))
                
                heapq.heappush(minHeap,(newDiff,nx,ny))
            
            
            