class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {}
        for i, s in enumerate(S):
            last[s] = i
            
        i, j, k = 0, 0, 0
        ans = []
        while i < len(S) and j < len(S):
            while i <= j:
                j = max(last[S[i]], j)
                if i == j:
                    break
                i += 1
            ans.append(j - k + 1)
            i, j, k = i + 1, j + 1, i + 1
            
        return ans
            