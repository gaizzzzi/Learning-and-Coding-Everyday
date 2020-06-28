class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        visited = set()
        self.ans = ""
        def helper(s):
            for i in range(k):
                suffix = str(i)
                if not s + suffix in visited:
                    visited.add(s + suffix)
                    helper(s[1:] + suffix)
                    self.ans += suffix
            
        helper("0" * (n - 1))
        return self.ans + "0" * (n - 1)