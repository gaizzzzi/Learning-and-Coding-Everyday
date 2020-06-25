class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip_points = []
        for num, start, end in trips:
            trip_points.append((start, 1, num))
            trip_points.append((end, -1, num))
        
        trip_points.sort()
        people = 0
        for location, is_start, num in trip_points:
            people += is_start * num
            if people > capacity:
                return False
        return True
        