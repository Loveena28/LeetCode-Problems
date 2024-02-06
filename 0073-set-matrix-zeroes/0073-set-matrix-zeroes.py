class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_index = []
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_index.append((i,j))
        for i in zero_index:
            for j in range(rows):
                matrix[j][i[1]] = 0
            for j in range(cols):
                matrix[i[0]][j] = 0