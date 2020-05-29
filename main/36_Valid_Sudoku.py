class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0] * 9
        col = [0] * 9
        box = [0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    d_bit = 1 << (int(board[i][j]) - 1)
                    if row[i] & d_bit or col[j] & d_bit or box[i // 3 * 3 + j // 3] & d_bit:
                        return False
                    row[i] |= d_bit
                    col[j] |= d_bit
                    box[i // 3 * 3 + j // 3] |= d_bit
                
        return True