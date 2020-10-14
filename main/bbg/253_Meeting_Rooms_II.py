class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        hp = []
        for start, end in intervals:
            if hp and hp[0][0] <= start:
                heappop(hp)
            heappush(hp, (end,start))
        return len(hp)