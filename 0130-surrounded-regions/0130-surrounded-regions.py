class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board),len(board[0])
        
        def dfs(i,j):
            board[i][j] = '#' # temporary marker
            directions = [(-1,0),(0,-1),(1,0),(0,1)]
            for x,y in directions:
                nx,ny = i+x,j+y
                if 0<=nx<rows and 0<=ny<cols and board[nx][ny] == 'O':
                    dfs(nx,ny)
        
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and(i==0 or i==rows-1 or j==0 or j==cols-1):
                    dfs(i,j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        
        return board
        
        