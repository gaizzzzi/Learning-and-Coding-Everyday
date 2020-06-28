class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        edges = []
        points = [p1, p2, p3, p4]
        
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i + 1:]:
                if not x2 - x1 and not y2- y1:
                    return False
                edges.append((x2 - x1, y2 - y1))
                
        parallel = 0
        ortho = 0
        for i, (x1, y1) in enumerate(edges):
            for x2, y2 in edges[i + 1:]:
                if x1 * y2 - x2 * y1 == 0:
                    parallel += 1
                if x1 * x2 + y1 * y2 == 0:
                    ortho += 1
        return ortho == 5 and parallel == 2