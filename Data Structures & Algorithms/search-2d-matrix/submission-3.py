class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        row = 0
        while l <= r:
            row = (l+r) // 2
            if matrix[row][0] > target:
                r = row - 1
            elif matrix[row][0] < target:
                if row + 1 < len(matrix) and matrix[row + 1][0] > target:
                    break
                l = row + 1
            else:
                return True

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            col = (l+r) // 2
            if matrix[row][col] > target:
                r = col - 1
            elif matrix[row][col] < target:
                l = col + 1
            else:
                return True
        return False
        