class Solution:
    def fib_On(self, N: int) -> int:
        if N == 0 or N == 1:
            return N
        fn1, fn2 = 0, 1
        for i in range(1, N):
            tmp = fn2
            fn2, fn1 = fn1 + fn2, tmp
        return fn2


    def fib_Ologn(self, n: int) -> int:
        if n == 0 or n == 1: return n
        positive_phi = (1 + 5 ** (1/2)) / 2
        negative_phi = (1 - 5 ** (1/2)) / 2
        def power(x, n):
            # logn calculate x ** n when n > 1 and n is integer
            if n == 1:
                return x
            if n == 0:
                return 1
            y = power(x, n // 2)
            
            return y * y * (x if n % 2 else 1) 
        return round((power(positive_phi, n) + power(negative_phi, n))/(5 ** (1/2)))