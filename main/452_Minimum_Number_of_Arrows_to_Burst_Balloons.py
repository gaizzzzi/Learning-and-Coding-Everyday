class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda x: x[0])
        arrow = 1
        pre_start, pre_end = points[0]
        for start, end in points[1:]:
            lo, hi = max(pre_start, start), min(end, pre_end)
            if lo <= hi:
                pre_start, pre_end = lo, hi
            else:
                arrow += 1
                pre_start, pre_end = start, end
        return arrow