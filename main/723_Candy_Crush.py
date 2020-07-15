class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        def helper(board):
            vertical = [[1] * len(board[0]) for _ in range(len(board))]
            horizontal = [[1] * len(board[0]) for _ in range(len(board))]
            change = 0
            
            # finding 消able candies
            for r, row in enumerate(board):
                for c, candy in enumerate(row):
                        if r and candy:
                            if candy == board[r - 1][c]:
                                vertical[r][c] += vertical[r - 1][c]
                        if c and candy:
                            if candy == board[r][c - 1]:
                                horizontal[r][c] += horizontal[r][c - 1]

            # 消candy horizontally
            for i in range(len(board)):
                n = 0
                for j in range(len(board[0]) - 1, -1, -1):
                    if not n and horizontal[i][j] > 2:
                        n = horizontal[i][j]
                        change += 1
                    if n:
                        board[i][j] = 0
                        n -= 1
            
            # 消candy vertically   
            for i in range(len(board[0])):
                n = 0
                for j in range(len(board) - 1, -1, -1):
                    if not n and vertical[j][i] > 2:
                        n = vertical[j][i]
                        change += 1
                    if n:
                        board[j][i] = 0
                        n -= 1
                        
            # swap to realize candy dropping
            for c in range(len(board[0])):
                i = j = len(board) - 1
                while i > -1 and j > -1:
                    while i > -1 and board[i][c] != 0:
                        i -= 1
                    j = min(i, j)
                    while j > -1 and board[j][c] == 0:
                        j -= 1
                    if j == -1:
                        continue
                    else:
                        board[i][c], board[j][c] = board[j][c], board[i][c]
                        
            return not change
            
        while not helper(board):
            pass
        return board
                
            
            
                    
                            