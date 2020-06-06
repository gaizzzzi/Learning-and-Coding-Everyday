class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # 02:30 - 03:29 wokule
        turns = 0
        is_X_win = [int(board[0][0] + board[1][1] + board[2][2] == "XXX") 
                    + int(board[0][2] + board[1][1] + board[2][0] == "XXX"), # diag-win count
                    0, # row-win count
                    0] # col-win count
        
        is_O_win = [int(board[0][0] + board[1][1] + board[2][2] == "OOO") 
                    + int(board[0][2] + board[1][1] + board[2][0] == "OOO"), # diag-win count
                    0, # row-win count
                    0] # col-win count
        
        for i in range(3):
            col = ""
            row = board[i]
            for j in range(3):
                if board[i][j] == "X":
                    turns += 1
                elif board[i][j] == "O":
                    turns -= 1
                col += board[j][i]
            if row == "XXX":
                is_X_win[1] += 1
            elif row == "OOO":
                is_O_win[1] += 1
            if col == "XXX":
                is_X_win[2] += 1
            elif col == "OOO":
                is_O_win[2] += 1
        
        
        # X should be larger than O
        if turns != 0 and turns != 1:
            return False
        
        # see if anyone wins
        if (is_X_win[1] > 1 or is_X_win[2] > 1) \
            or (is_O_win[0] > 1 or is_O_win[1] > 1 or is_O_win[2] > 1) \
            or (sum(is_X_win) > 0 and sum(is_O_win) > 0) \
            or (turns == 0 and sum(is_X_win)  > 0) \
            or (turns == 1 and sum(is_O_win) > 0):
            return False
        
        return True
        
        
        