class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def helper(solution_set, current_sum, pos):
            if current_sum == target:
                ans.append(solution_set)
                return
            for i in range(pos, len(candidates)):
                if current_sum + candidates[i] > target:
                    return
                helper(solution_set + [candidates[i]], current_sum + candidates[i], i)
        helper([], 0, 0)
        return ans