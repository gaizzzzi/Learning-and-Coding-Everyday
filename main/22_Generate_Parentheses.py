class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 20:03 - 20:08
        ans = []
        def helper(left, right, path):
            if not left and not right:
                ans.append(path)
            if left > 0:
                helper(left - 1, right, path + "(")
            if left < right:
                helper(left, right - 1, path + ")")
        helper(n, n, "")
        return ans