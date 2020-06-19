class SnapshotArray_timeout:
    
    def __init__(self, length: int):
        self.array = [0] * length
        self.snapshot = {}
        self.snapid = -1
    def set(self, index: int, val: int) -> None:
        self.array[index] = val

    def snap(self) -> int:
        self.snapid += 1
        self.snapshot[self.snapid] = copy.deepcopy(self.array)
        return self.snapid

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshot[snap_id][index]

class SnapshotArray_binary_search:

    def __init__(self, length: int):
        self.array = [[[0, 0]] for _ in range(length)]
        self.snapid = 0
        
    def set(self, index: int, val: int) -> None:
        if self.array[index][-1][0] == self.snapid:
            self.array[index][-1][1] = val
        else:
            self.array[index].append([self.snapid, val])

    def snap(self) -> int:
        self.snapid += 1
        return self.snapid - 1

    def get(self, index: int, snap_id: int) -> int:
        history = self.array[index]
        start, end = 0, len(history) - 1
        while start < end - 1:
            mid = (start + end) // 2
            if history[mid][0] == snap_id:
                return history[mid][1]
            elif history[mid][0] < snap_id:
                start = mid
            else:
                end = mid
            
        if history[end][0] <= snap_id:
            return history[end][1]
        return history[start][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)