class UndergroundSystem:

    def __init__(self):
        self.passenger_id = {} # {id: startstation}
        self.average_time = {} # {(startstation, endstation): (avgtime, times)}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passenger_id[id] = (stationName, t) 

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.passenger_id[id]
        avgtime, times = self.average_time.get((startStation, stationName), (0, 0))
        self.average_time[(startStation, stationName)] = ((avgtime * times + t - startTime) / (times + 1), times + 1)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.average_time.get((startStation, endStation))[0]


class UndergroundSystem:

    def __init__(self):
        self.passenger = defaultdict(list) # {id: [startStation, startTime]}
        self.avg_time = defaultdict(list) # {(startStation, endStation): [avgTime, count]}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passenger[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.passenger[id]
        avgtime, count = self.avg_time.get((start_station, stationName), [0.0, 0.0])
        self.avg_time[(start_station, stationName)] = [(avgtime * count + (t - start_time))/ (count + 1), count + 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg_time[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)