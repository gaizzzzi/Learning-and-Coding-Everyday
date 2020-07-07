class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        row_up, row_down, col_left, col_right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        i, j, ans = 0, 0, [matrix[0][0]]
        while row_down >= row_up and col_left <= col_right:
            while row_down >= row_up and j < col_right:
                j += 1
                ans.append(matrix[i][j])
            row_up += 1
            
            while col_left <= col_right and i < row_down:
                i += 1
                ans.append(matrix[i][j])
            col_right -= 1
            
            while row_down >= row_up and j > col_left:
                j -= 1
                ans.append(matrix[i][j])
            row_down -= 1
            
            while col_left <= col_right and i > row_up:
                i -= 1
                ans.append(matrix[i][j])
            col_left += 1
        return ans
                
            