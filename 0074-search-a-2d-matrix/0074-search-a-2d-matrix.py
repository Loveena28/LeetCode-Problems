class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numberOfRows,numberOfCols = len(matrix), len(matrix[0])
        top,bottom = 0,numberOfRows - 1
        while top <= bottom:
            mid = top + (bottom-top) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                break
        if not(top <= bottom):
            return False
        r = (top+bottom)//2
        left,right = 0,numberOfCols - 1
        while left <= right:
            mid = left + (right-left)//2
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False    