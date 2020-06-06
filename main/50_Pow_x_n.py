class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 19:26 - 19:30
        if n == 0:
            return 1
        
        if n < 0:
            return 1/self.myPow(x, -n)
        
        tmp = self.myPow(x, abs(n) // 2)
        
        if n & 1:
            return tmp * tmp * x

        return tmp * tmp