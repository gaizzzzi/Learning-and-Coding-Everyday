class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # one pass
        left = []
        ans = ""
        for char in s:
            if char == ")" and not left:
                continue
            if char == "(":
                left.append(len(ans))
            if char == ")":
                left.pop()
            ans += char
            
        while left:
            i = left.pop()
            ans = ans[:i] + ans[i+1:]
        
        return ans