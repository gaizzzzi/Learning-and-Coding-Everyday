class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        # 17:54 - 17:57 one pass
        ans = []
        for l, r in intervals:
            
            if l < toBeRemoved[0] < r:
                ans.append([l, toBeRemoved[0]])
            if l < toBeRemoved[1] < r:
                ans.append([toBeRemoved[1], r])
            if toBeRemoved[1] < l or toBeRemoved[0] > r:
                ans.append([l, r])
                
        return ans