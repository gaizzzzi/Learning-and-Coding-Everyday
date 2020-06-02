class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        def operations(nums, a):
            out = []
            for b in nums:
                if a != 0:
                    out += [b * a, b + a, b / a, b - a]
                else:
                    out += [b * a, b + a, b - a]
            return out
        def helper(nums):
            a = [nums[0], nums[2]]
            b = [nums[1], nums[3]]
            
            tmp_out = []
            for i in range(2):
                tmp_out.append(operations([a[i]], b[i]))
            
            
            for i in range(4):
                for j in range(4):
                    out = operations([tmp_out[0][i]], tmp_out[1][j])
                    for o in out:
                        if abs(o) == 24 or abs(abs(o) - 1/24) < 0.0001:
                            return True
            return False
    
        n = sum(nums) 
        for i in range(4):
            a = nums[i]
            for j in range(4):
                if j == i:
                    continue
                b = nums[j]
                out = operations([a], b)
                for k in range(4):
                    if i == k or j == k:
                        continue
                    c = nums[k]
                    out1 = operations(out, c)
                    d = n - a - b - c
                    out2 = operations(out1, d)
                    for o in out2:
                        if abs(o) == 24 or abs(abs(o) - 1/24) < 0.0001:
                            return True
                    # calc (a,b) (c,d)
                    if helper([a,b,c,d]):
                        return True
                    
            
        return False
            
            