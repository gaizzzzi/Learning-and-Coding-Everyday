class Solution:
    def isHappy(self, n: int) -> bool:
        # one pass
        square_sum = n
        visited = {}
        while square_sum != 1 and not square_sum in visited:
            visited.add(square_sum)
            tmp = 0
            while square_sum:
                tmp += (square_sum % 10) ** 2
                square_sum //= 10
            square_sum = tmp

        return square_sum == 1