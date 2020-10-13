class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                neibor_lives = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if (not di and not dj):
                            continue
                        if -1 < i + di < len(board) and -1 < j + dj < len(board[0]):
                            neibor_lives += int(board[i + di][j + dj] > 0)
                if board[i][j] and (neibor_lives < 2 or neibor_lives >3):
                    board[i][j] = 2
                if not board[i][j] and neibor_lives == 3:
                    board[i][j] = -1
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] > 1:
                    board[i][j] = 0
                elif board[i][j] < 0:
                    board[i][j] = 1