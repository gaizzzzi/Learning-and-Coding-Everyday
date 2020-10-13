from heapq import heappop, heappush, heapify
def solver(sticks):
    #heapify(sticks)
    effort = 0
    while len(sticks) > 1:
        curr_effort = heappop(sticks) + heappop(sticks)
        print(curr_effort)
        effort += curr_effort
        heappush(sticks, curr_effort)
    return effort

sticks = [2, 4, 3]
sticks = [8, 5, 3]
#sticks = [5]
print(solver(sticks))