class Fibonacci:
    def bottom_up(self, n):
        # o(2^n)
        if n == 0 or n == 1:
            return 1
        
        return self.bottom_up(n-1) + self.bottom_up(n-2)

    def top_down(self, n):

        if n == 0 or n == 1:
            return 1

        def top_down_helper(i, fib_1, fib_2):
            if i == n:
                return fib_2
            
            return top_down_helper(i + 1, fib_2, fib_1 + fib_2)


        return top_down_helper(1, 1, 1)
        

    def DP(self, n):
        # o(n) + o(n)
        fib_list = [0] * (n + 1)
        fib_list[0] = 1
        fib_list[1] = 1 

        i = 2

        while i <= n:
            fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
            i += 1

        return fib_list[n]

# test
f = Fibonacci()
n = 7
print(f.bottom_up(n))
print(f.top_down(n))
print(f.DP(n))