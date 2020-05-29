class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False] * len(board[0]) for i in range(len(board))]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs_helper(pos, depth, visited):
            if depth == len(word) - 1:
                return True
            x, y = pos
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < len(board) and 0 <= new_y < len(board[0])and not visited[new_x][new_y]:
                    if board[new_x][new_y] == word[depth + 1]:
                        visited[new_x][new_y] = True
                        if_match = dfs_helper((new_x, new_y), depth + 1, visited)
                        if if_match: 
                            return True
                        visited[new_x][new_y] = False
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if_match = dfs_helper((i, j), 0, visited)
                    if if_match:
                        return True
                    visited[i][j] = False
        return False