class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        visited = set()
        graph = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def helper(_x, _y, x, y):
            tmp_path = set()
            for dx, dy in directions:
                newx, newy = x + dx, y + dy
                if -1 < newx < len(grid) and -1 < newy < len(grid[0]) and \
                    grid[newx][newy] and not (newx, newy) in visited:
                        visited.add((newx, newy))
                        tmp_path.add((newx - _x, newy - _y))
                        tmp_path.update(helper(_x, _y, newx, newy))
            
            return tmp_path
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and not (i, j) in visited:
                    graph.add(frozenset(helper(i, j, i, j)))
        return len(graph)