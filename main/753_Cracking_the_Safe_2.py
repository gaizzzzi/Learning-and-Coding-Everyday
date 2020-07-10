class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        visited, ans = {"0"*n}, []
        def helper(s):
            for i in range(k):
                tmp = s[1:] + str(i)
                if not tmp in visited:
                    visited.add(tmp)
                    helper(tmp)
            ans.append(s[0])
        helper('0' * n)
        return "".join(ans[::-1]) + '0' * (n - 1)