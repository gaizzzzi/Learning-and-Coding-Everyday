import queue
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        visited = set([0])
        q = queue.Queue()
        q.put(0)
        num = {}
        for i, a in enumerate(arr):
            if a in num:
                num[a].append(i)
            else:
                num[a] = [i]
        
        step = 0
        while not q.empty():
            n = q.qsize()
            while n:
                n -= 1
                idx = q.get()
                if idx == len(arr) - 1:
                    return step
                if not idx + 1 in visited and idx + 1 < len(arr):
                    q.put(idx + 1)
                    visited.add(idx + 1)
                if not idx - 1 in visited and idx - 1 >= 0:
                    q.put(idx - 1)
                    visited.add(idx - 1)
                for next_idx in num[arr[idx]]:
                    if not next_idx in visited:
                        q.put(next_idx)
                        visited.add(next_idx)
                num[arr[idx]] = []
            step += 1

