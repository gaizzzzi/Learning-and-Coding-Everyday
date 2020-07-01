class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # 18:53 - 18:59 one pass
        visited = set((sr, sc))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def helper(_x, _y, old_color):
            for dx, dy in directions:
                x, y = _x + dx, _y + dy
                if -1 < x < len(image) and -1 < y < len(image[0]) and image[x][y] == old_color and not (x, y) in visited:
                    visited.add((x, y))
                    image[x][y] = newColor
                    helper(x, y, old_color)
                    
        old_color, image[sr][sc] = image[sr][sc], newColor
        helper(sr, sc, old_color)
        return image