class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def helper(depth, curr, visited):
            if depth == len(nums):
                res.append(curr)
                return
            last_idx = -1
            for i in range(len(nums)):
                if i in visited:
                    continue
                if last_idx != -1 and nums[last_idx] == nums[i]:
                    continue
                visited.add(i)
                last_idx = i
                helper(depth + 1, curr + [nums[i]], visited)
                visited.remove(i)
        helper(0, [], set())
        return res
        
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        for num in nums:
            tmp = []
            for r in res:
                for k in range(len(r) + 1):
                    if k and num == r[k - 1]:
                        break
                    tmp.append(r[:k] + [num] + r[k:])
            res = tmp
        return res