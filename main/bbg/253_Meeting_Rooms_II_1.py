class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        hp = []
        for start, end in intervals:
            if not hp or hp[0] > start:
                heappush(hp, end)
            else:
                heappushpop(hp, end)
        return len(hp)