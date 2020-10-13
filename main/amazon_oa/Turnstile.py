from collections import deque
def solver(numcustomers, arrTime, direction):
    res = [[0] for i in range(numcustomers)]
    enter, exit = deque(), deque()
    for i in range(numcustomers):
        if direction[i]:
            exit.append((arrTime[i], i))
        else:
            enter.append((arrTime[i], i))

    curr_time, curr_status = 0, 1
    while enter or exit:
        if curr_status and exit and exit[0][0] <= curr_time:
            _, idx = exit.popleft()
            res[idx] = curr_time
            curr_time += 1
        elif not curr_status and enter and enter[0][0] <= curr_time:
            _, idx = enter.popleft()
            res[idx] = curr_time
            curr_time += 1
        elif exit and exit[0][0] <= curr_time:
            _, idx = exit.popleft()
            res[idx] = curr_time
            curr_time += 1
            curr_status = 1
        elif enter and enter[0][0] <= curr_time:
            _, idx = enter.popleft()
            res[idx] = curr_time
            curr_time += 1
            curr_status = 0
        else:
            curr_status = 1
            if enter:
                curr_time = enter[0][0]
            if exit:
                curr_time = min(exit[0][0], curr_time)
    return res
n, arr, dire = 4, [0,0,1,5], [0,1,1,0]
n, arr, dire = 5, [0,1,1,3,3], [0,1,0,0,1]
n, arr, dire = 5, [0,1,1,4,4], [1,0,1,0,1]
n, arr, dire = 5, [0,1,1,4,4], [1,0,1,0,0]
#n, arr, dire = 5, [0,1,1,3,3], [0,1,0,0,1]
#n, arr, dire = 5, [0,1,1,3,3], [0,1,0,0,1]
print(solver(n, arr, dire))
    


