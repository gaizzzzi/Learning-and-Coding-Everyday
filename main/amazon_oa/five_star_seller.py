import heapq
def solver(productRatings, ratingsThreshold):
    hp, n, avg = [], len(productRatings), 0
    for i, (x, y) in enumerate(productRatings):
        heapq.heappush(hp, (-(x + 1) / (y + 1) + x / y , x, y))
        avg = (avg * i + x / y) / (i + 1)

    
    count = 0
    while avg * 100 < ratingsThreshold:
        _, x, y = heapq.heappop(hp)
        avg = (avg * n - x / y + (x + 1) / (y + 1)) / n
        x, y = x + 1, y + 1
        heapq.heappush(hp, (-(x + 1) / (y + 1) + x / y, x, y))
        count += 1
        
    return count
proR, thre = [[4,4],[1,2],[3,6]], 77
print(solver(proR, thre))