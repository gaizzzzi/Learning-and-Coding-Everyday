class Solution:
    def maxLength(self, arr: List[str]) -> int:
        s_sets = [set()]
        for s in arr:
            tmp = set(s)
            if len(s) != len(tmp):
                continue
            for s_set in s_sets:
                if not tmp & s_set:
                    s_sets.append(tmp | s_set)
        return max([len(x) for x in s_sets])