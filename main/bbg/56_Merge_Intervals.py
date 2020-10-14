class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = []
        prestart, preend = intervals[0]
        for start, end in intervals[1:]:
            if preend >= start:
                preend = max(end, preend)
            else:
                res.append([prestart, preend])
                prestart, preend = start, end
        res.append([prestart, preend])
        return res
        