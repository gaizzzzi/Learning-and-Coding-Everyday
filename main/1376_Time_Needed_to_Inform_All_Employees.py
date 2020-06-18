import queue
class Solution:
    def numOfMinutes_bfs_2964ms(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        emp_map = {}
        for subor, manager in enumerate(manager):
            emp_map[manager] = emp_map.get(manager, []) + [subor]
            
        ans = 0
        q = queue.Queue()
        q.put((-1, 0))
        people = 0
        while not q.empty():
            emp, time = q.get()
            if not emp in emp_map:
                continue
            for sub in emp_map[emp]:
                people += 1
                q.put((sub, informTime[sub] + time))
                if ans < informTime[sub] + time:
                    ans = informTime[sub] + time
        return ans

    def numOfMinutes_dfs_1584ms(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        emp_map = {}
        for subor, manager in enumerate(manager):
            emp_map[manager] = emp_map.get(manager, []) + [subor]
            
        def helper(emp):
            return (max([helper(sub) for sub in emp_map.get(emp)]) if emp in emp_map else 0) + informTime[emp]
        
        return helper(headID)