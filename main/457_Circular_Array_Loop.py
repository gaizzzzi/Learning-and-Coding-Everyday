class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if not nums:
            return False
        idx_map = {}
        def helper(pos, coll):
            step_map = {}
            step = 0
            while not pos in idx_map:
                coll.append(pos)
                idx_map[pos] = step
                step_map[step] = pos
                step += 1
                pos = (pos + nums[pos]) % len(nums)
            if step - idx_map[pos] == 1 or not pos in coll:
                return False
            start = idx_map[pos]
            sign_flag = nums[pos] > 0
            for i in range(start, step):
                if (sign_flag > 0) ^ (nums[step_map[i]] > 0):
                    return False
            return True
        
        for i in range(len(nums)):
            if not i in idx_map:
                if helper(i, []):
                    return True
        
        return False