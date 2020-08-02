class UndergroundSystem:
    # one pass

    def __init__(self):
        self.passenger = defaultdict(tuple)
        self.travel_time = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passenger[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station_key = (self.passenger[id][1], stationName)
        if not station_key in self.travel_time:
            self.travel_time[station_key].extend([0, 0])
        self.travel_time[station_key][1] += t - self.passenger[id][0]
        self.travel_time[station_key][0] += 1
        self.passenger.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if not (startStation, endStation) in self.travel_time:
            return 0
        return self.travel_time[(startStation, endStation)][1]/self.travel_time[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)