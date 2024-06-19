class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        queue = deque()
        queue.append((sr,sc))
        original_color = image[sr][sc]
        
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        
        while queue:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                image[x][y] = color
                for dx,dy in directions:
                    nx,ny = x+dx,y+dy
                    if (nx >=0 and nx < len(image)) and (ny >= 0 and ny < len(image[0])) and (image[nx][ny] == original_color):
                        image[nx][ny] = color
                        queue.append((nx,ny))
        return image