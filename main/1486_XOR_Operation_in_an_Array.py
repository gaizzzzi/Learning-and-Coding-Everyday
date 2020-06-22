class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans, tmp = 0, start
        for i in range(n):
            #print( tmp)
            ans ^= tmp
            tmp += 2
        return ans