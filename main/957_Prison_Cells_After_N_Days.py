class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def to_list(num):
            tmp = []
            for i in range(8):
                tmp.append(num & 1)
                num >>= 1
            return tmp
        
        cells_set = []
        days = 0
        while days < N:
            num = 0
            for i, occupied in enumerate(cells):
                num |= occupied << i
            if num in cells_set:
                idx = cells_set.index(num)
                return to_list(cells_set[(N - idx) % (days - idx) + idx])
            
            cells_set.append(num)
            tmp = [0] * 8
            for i in range(1, 7):
                tmp[i] = int(cells[i - 1] == cells[i + 1])
            cells = tmp
            
            days += 1
        return cells
        
        