import queue
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 20:31 - 20:43
        dead = set(deadends)
        q = queue.Queue()
        if target in dead or '0000' in dead:
            return -1
        q.put('0000')
        depth = 0
        visited = {'0000'}
        
        while not q.empty():
            depth += 1
            n = q.qsize()
            while n:
                n -= 1
                wheels = q.get()
                for i in range(4):
                    for move in (-1, 1):
                        tmp = wheels[:i] + str((int(wheels[i]) + move) % 10) + wheels[i + 1:]
                        if tmp == target:
                            return depth
                        
                        if not tmp in visited and not tmp in dead:
                            visited.add(tmp)
                            q.put(tmp)
                
        return -1
                
                   