class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        row = len(matrix)
        col = len(matrix[0])
        

        for r in range(row):
            if target <= matrix[r][-1] and target >=  matrix[r][0]:
                for c in range(col):
                    if matrix[r][c] == target:
                        return True
           
        return False
        