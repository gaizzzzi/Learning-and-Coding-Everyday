import collections
def solver(grid):
    q = collections.deque()
    q.append((0, 0, 0))
    visited = {(0, 0)}
    while q:
        i, j, step = q.popleft()
        for ni, nj in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
            if -1 < ni < len(grid) and -1 < nj < len(grid[0]) and not (ni, nj) in visited and grid[ni][nj] != 'D':
                if grid[ni][nj] == 'X':
                    return step + 1
                q.append((ni, nj, step + 1))
                visited.add((ni, nj))
    return -1
grid = [['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

print(solver(grid))

