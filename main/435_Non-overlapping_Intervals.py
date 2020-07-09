class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        skip = 0
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[1])
        pre_start, pre_end = intervals[0]
        for start, end in intervals[1:]:
            if start < pre_end:
                skip += 1
            else:
                pre_start, pre_end = start, end
        return skip
# nlogn