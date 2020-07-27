# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        available_rows = [i for i in range(m)]
        tmp = []
        left, right = 0, n - 1
        while left < right - 1:
            mid = (left + right) // 2
            for row in available_rows:
                if binaryMatrix.get(row, mid):
                    tmp.append(row)
            if not tmp:
                left = mid
            else:
                right = mid
                available_rows = tmp
                tmp = []
        if any(binaryMatrix.get(x, left) for x in available_rows):
            return left
        if any(binaryMatrix.get(x, right) for x in available_rows):
            return right
        return -1