class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 02：15 - 02: 24
        directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), 
                      (1, 0), (1, 1), (0, 1), (-1, 1)]
        
        # update next stage with dead -> live = -2, live -> dead = 2 
        for i in range(len(board)):
            for j in range(len(board[0])):
                live = 0
                dead = 0
                for di, dj in directions:
                    new_i, new_j = i + di, j + dj
                    if -1 < new_i < len(board) and -1 < new_j < len(board[0]):
                        live += int(board[new_i][new_j] > 0)
                        dead += int(board[new_i][new_j] < 1)
                if board[i][j] and (live < 2 or live > 3):
                    board[i][j] = 2
                elif not board[i][j] and live == 3:
                    board[i][j] = -2
        
        # transfer the mid stage to final stage
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -2:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0