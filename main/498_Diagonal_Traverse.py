class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        dia_list = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dia_list[i + j].append(matrix[i][j])
        ans = []
        for idx, item in sorted(dia_list.items()):
            if idx % 2:
                ans.extend(item)
            else:
                ans.extend(item[::-1])
        return ans
        
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        ans = []
        for i in range(len(matrix) + len(matrix[0]) - 1):
            if not i % 2:
                for x in range(min(i, len(matrix) - 1), max(-1, i - len(matrix[0])), -1):
                    y = i - x
                    ans.append(matrix[x][y])
            else:
                for y in range(min(i, len(matrix[0]) - 1), max(-1, i - len(matrix)), -1):
                    x = i - y
                    ans.append(matrix[x][y])
        return ans