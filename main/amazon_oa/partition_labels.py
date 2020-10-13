class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_idx = {}
        for i in range(len(S)):
            last_idx[S[i]] = i

        start, end = 0, 0
        res = []
        for i in range(len(S)):
            end = max(last_idx[S[i]], end)
            if end == i:
                res.append(end - start + 1)
                start = end + 1

        return res
