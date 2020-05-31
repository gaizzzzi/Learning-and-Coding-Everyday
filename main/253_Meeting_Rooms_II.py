class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = []
        for start, end in intervals:
            times.append((start, 1))
            times.append((end, 0))
        times.sort()
        rooms = 0
        rooms_rolling = 0
        for t, is_start in times:
            if is_start:
                rooms_rolling += 1
                rooms = max(rooms, rooms_rolling)
            else:
                rooms_rolling -= 1
        return rooms