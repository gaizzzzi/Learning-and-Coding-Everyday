class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        vertical_pairs = {}
        min_area, prev_x, prev_y = float('inf'), float('-inf'), []
        for x, y in points:
            if x == prev_x:
                for _y in prev_y:
                    if y == _y:
                        continue
                    if vertical_pairs.get((_y, y)) != None and vertical_pairs.get((_y, y)) != x:
                        min_area = min(min_area, (y - _y) * (x - vertical_pairs.get((_y, y))))
                    vertical_pairs[(_y, y)] = x
            else:
                prev_x, prev_y = x, []
            prev_y.append(y)
        return 0 if min_area == float('inf') else min_area

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set(map(tuple,points))
        min_area = float('inf')
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[:i]:
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        min_area = min(min_area, abs((x2 - x1) * (y2 - y1)))
        return min_area if min_area != float('inf') else 0
                