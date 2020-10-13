class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        pack = sorted(zip(indexes, sources, targets))
        prev_idx, outputS = 0, ""
        for idx, source, target in pack:
            if idx + len(source) <= len(S) and S[idx:idx + len(source)] == source:
                if prev_idx < idx:
                    outputS += S[prev_idx:idx]
                outputS += target
                prev_idx = idx + len(source)
        if prev_idx < len(S):
            outputS += S[prev_idx:]
        return outputS
        