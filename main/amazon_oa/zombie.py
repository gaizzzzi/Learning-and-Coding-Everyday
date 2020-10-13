import queue
def minHours(rows, columns, grid):

	moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
	q = queue.Queue() # (row, col, step)
	zombie_set = set() # visited
	for i in range(rows):
		for j in range(columns):
			if grid[i][j]:
				q.put((i, j, 0))
				zombie_set.add((i, j))

	while not q.empty():
		i, j, step = q.get()
		for di, dj in moves:
			ni, nj = i + di, j + dj
			if -1 < ni < rows and -1 < nj < columns and not (ni, nj) in zombie_set:
				zombie_set.add((ni, nj))
				q.put((ni, nj, step + 1))

	return step if len(zombie_set) == rows * columns else -1
