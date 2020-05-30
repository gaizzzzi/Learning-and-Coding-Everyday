class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        ans = []
        def helper(nums, pos, cur_sum):
            if pos  == len(candidates):
                return
            last_i = pos
            for i in range(pos, len(candidates)):
                if cur_sum + candidates[i] == target:
                    ans.append(nums + [candidates[i]])
                    return
                elif cur_sum + candidates[i] < target:
                    if last_i != i and candidates[last_i] == candidates[i]:
                        continue
                    
                    helper(nums + [candidates[i]], i + 1, cur_sum + candidates[i])
                last_i = i
        
        helper([], 0, 0)
        return ans