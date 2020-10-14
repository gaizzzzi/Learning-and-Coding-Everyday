class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        if not board:
            return []
        rerun = False
        rows, cols = len(board), len(board[0])
        for row in range(rows - 2):
            for col in range(cols):
                if board[row][col] == 0:
                    continue
                if abs(board[row][col]) == abs(board[row + 1][col]) == abs(board[row + 2][col]):
                    board[row][col] = board[row + 1][col] = board[row + 2][col] = -abs(board[row][col])
                    rerun = True
                    
        for col in range(cols - 2):
            for row in range(rows):
                if board[row][col] == 0:
                    continue
                if abs(board[row][col]) == abs(board[row][col + 1]) == abs(board[row][col + 2]):
                    board[row][col] = board[row][col + 1] = board[row][col + 2] = -abs(board[row][col])
                    rerun = True
                    
        for col in range(cols):    
            down = rows - 1
            for up in range(rows - 1, -1, -1):
                if board[up][col] > 0:
                    board[down][col] = board[up][col]
                    down -= 1
            for row in range(down, -1, -1):
                board[row][col] = 0
                
        return self.candyCrush(board) if rerun else board