class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i,len(matrix[0])):
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        def reverse_rows(matrix):
            for i in range(len(matrix)):
                left,right = 0,len(matrix)-1
                while left<right:
                    matrix[i][left],matrix[i][right] = matrix[i][right],matrix[i][left]
                    left = left+1
                    right = right -1
        transpose(matrix)
        reverse_rows(matrix)
        