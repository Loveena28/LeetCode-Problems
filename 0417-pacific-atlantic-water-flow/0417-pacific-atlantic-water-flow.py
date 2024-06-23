class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = [[False for _ in range(n)] for _ in range(m)]
        atlantic = [[False for _ in range(n)] for _ in range(m)]
        res = []

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        def get_neighbours(x, y):
            neighbours = []
            for dirx, diry in dirs:
                newx, newy = x+dirx, y+diry
                if 0 <= newx < m and 0 <= newy < n:
                    neighbours.append((newx, newy))
            return neighbours

        def dfs(x, y, ocean):
            if ocean[x][y]: return
            ocean[x][y] = True
            for newx, newy in get_neighbours(x,y):
                if heights[newx][newy] >= heights[x][y]:
                    dfs(newx, newy, ocean)

        for x in range(m):
            dfs(x, 0, pacific)
            dfs(x, n-1, atlantic)
        for y in range(n):
            dfs(0, y, pacific)
            dfs(m-1, y, atlantic)

        for x in range(m):
            for y in range(n):
                if pacific[x][y] and atlantic[x][y]:
                    res.append([x,y])
        return res

