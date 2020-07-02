class Solution:
    # 20:37 - 20:53
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        a = [[0] * len(board[0]) for _ in range(len(board))]
        for _x in range(len(a)):
            for _y in range(len(a[0])):
                if board[_x][_y] == "M":
                    for dx, dy in directions:
                        x, y = _x + dx, _y + dy
                        if -1 < x < len(a) and -1 < y < len(a[0]):
                            a[x][y] += 1
                            
        def helper(_x, _y):
            if board[_x][_y] == "E" and not a[_x][_y]:
                board[_x][_y] = "B"
                for dx, dy in directions:
                    x, y = _x + dx, _y + dy
                    if -1 < x < len(a) and -1 < y < len(a[0]):
                        helper(x, y)
            elif board[_x][_y] == "E":
                board[_x][_y] = str(a[_x][_y])
                
        helper(click[0], click[1])
        return board


    # reduced adundant spaces
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                            
        def helper(_x, _y):
            if board[_x][_y] != "E":
                return
            count = 0
            for dx, dy in directions:
                x, y = _x + dx, _y + dy
                if -1 < x < len(board) and -1 < y < len(board[0]):
                    count += int(board[x][y] == "M")
            
            if count:
                board[_x][_y] = str(count)
            else:
                board[_x][_y] = "B"
                for dx, dy in directions:
                    x, y = _x + dx, _y + dy
                    if -1 < x < len(board) and -1 < y < len(board[0]):
                        helper(x, y)
                
        helper(click[0], click[1])
        return board
            
            