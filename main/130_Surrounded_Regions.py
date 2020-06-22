class Solution:
    def solve_dfs_148ms(self, board: List[List[str]]) -> None:
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


    def solve_Union_find_316ms(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 00:42
        if not board:
            return board
        parent = [i for i in range(len(board) * len(board[0]) + 1)]
        rank = [0] * (len(board) * len(board[0]) + 1)

        
        def find_parent(x):
            #print(x)
            while abs(x) != abs(parent[abs(x)]):
                parent[abs(x)] = parent[abs[parent[abs(x)]]]
                x = parent[abs(x)]
            return parent[abs(x)]

        def union(x, y):
            parent_x, parent_y = find_parent(x), find_parent(y)
            
            if parent_x == parent_y:
                return
            if parent_x < 0 and parent_y > 0:
                parent[parent_y] = parent_x
            elif parent_y < 0 and parent_x > 0:
                parent[parent_x] = parent_y
            elif rank[abs(parent_x)] < rank[abs(parent_y)]:
                parent[abs(parent_x)] = parent_y
            elif rank[abs(parent_x)] > rank[abs(parent_y)]:
                parent[abs(parent_y)] = parent_x
            else:
                parent[abs(parent_y)] = parent_x
                rank[abs(parent_x)] += 1

        # initilize the parent of edge to negative itslef
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1) and board[i][j] == "O":
             
                    parent[j + i * len(board[0]) + 1] = - (j + i * len(board[0]) + 1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j]) == "X":
                    continue
                for di, dj in [[1, 0], [0, 1]]:
                    new_i, new_j = i + di, j + dj
                    
                        
                    if new_i < len(board) and new_j < len(board[0]) and board[new_i][new_j] == "O":
                        union(new_i * len(board[0]) + new_j + 1, i * len(board[0]) + j + 1)
                        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 16 and j == 7:
                    a = 1
                    pass
                if board[i][j] == "O":
                    if find_parent(j + i * len(board[0]) + 1) > 0:
                        
                        board[i][j] = "X"

# 20:41 - 20:50
class unionfind:
    def __init__(self, m, n):
        self.prt = [i for i in range(n * m + 1)]
        self.rk = [0 for _ in range(n * m + 1)]
    
    def find(self, x):
        while self.prt[x] != x:
            self.prt[x] = self.prt[self.prt[x]]
            x = self.prt[x]
        return x
    
    def union(self, _x, _y):
        x, y = self.find(_x), self.find(_y)
        if x == y:
            return
        if self.rk[x] < self.rk[y]:
            self.prt[x] = y
            self.rk[y] += 1
        else:
            self.prt[y] = x
            self.rk[x] += 1
    
    def is_edge(self, x):
        
        return self.find(x) == self.find(len(self.prt) - 1)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        m, n = len(board), len(board[0])
        uf = unionfind(m, n)
        
        # build union find
        for r, row in enumerate(board):
            for c, letter in enumerate(row):
                if letter == "O":
                    if r and board[r - 1][c] == "O":
                        uf.union(r * n + c, (r - 1) * n + c)
                    if c and board[r][c - 1] == "O":
                        uf.union(r * n + c, r * n + c - 1)
                    if not r or not c or r == m - 1 or c == n - 1:
                        uf.union(r * n + c, m * n)
                        
        # flip
        for r, row in enumerate(board):
            for c, letter in enumerate(row):
                if letter == "O" and not uf.is_edge(r * n + c):
                    board[r][c] = "X"
                    
                        
      




      
                                
                                
                    
                    
            