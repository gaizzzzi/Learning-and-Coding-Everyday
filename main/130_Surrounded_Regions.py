class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #20:36
        if not board:
            return board
        
        def dfs_helper(x, y):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return
            
            if board[x][y] == "O":
                board[x][y] = "W"
                dfs_helper(x - 1, y)
                dfs_helper(x + 1, y)
                dfs_helper(x, y - 1)
                dfs_helper(x, y + 1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1):
                    
                    dfs_helper(i, j)
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "W":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
      
                                
                                
                    
                    
            