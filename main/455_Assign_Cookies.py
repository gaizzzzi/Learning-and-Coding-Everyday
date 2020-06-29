class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 18:17 - 18:24 one pass
        g.sort()
        s.sort()
        def helper(cookie):
            l, r = 0, len(s) - 1
            while l < r - 1:
                mid = (l + r) // 2
                if s[mid] == cookie:
                    return mid
                elif s[mid] < cookie:
                    l = mid
                else:
                    r = mid
            if s[l] >= cookie:
                return l
            if s[r] >= cookie:
                return r
            return None
        
        i, ans = 0, 0
        while s and i < len(g) and g[i] <= s[-1]:
            j = helper(g[i])
            if not j is None:
                ans += 1
                s.pop(j)
                i += 1
            
        return ans