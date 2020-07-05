import queue
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def get_index(num, n):
            tmp = (num - 1) // n
            x = len(board) - tmp - 1
            y = (num - 1) % n
            if tmp & 1:
                y = n - y - 1
            return(x, y)
        n = len(board)
        q, visited, depth = queue.Queue(), {1}, 0
        q.put(1)
        while not q.empty():
            qsize = q.qsize()
            depth += 1
            while qsize:
                qsize -= 1
                square = q.get()
                for i in range(1, 7):
                    x, y = get_index(square + i, n)
                    if board[x][y] == n * n or square + i == n * n:
                        return depth
                    elif board[x][y] != -1:
                        if not board[x][y] in visited:
                            visited.add(board[x][y])
                            q.put(board[x][y])
                    elif not square + i in visited:
                        visited.add(square + i)
                        q.put(square + i)
        return -1