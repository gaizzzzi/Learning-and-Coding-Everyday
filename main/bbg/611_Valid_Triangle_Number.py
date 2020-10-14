class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        def largest_edge_idx(lo, hi, target):
            l, r = lo, hi
            while l < r - 1:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid
                else:
                    r = mid
            if nums[r] < target:
                return r
            return l
        
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                idx = largest_edge_idx(j, len(nums) - 1, nums[i] + nums[j])
                res += idx - j
        return res

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i + 1, len(nums) - 1):
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                res += k - j - 1
        return res
                
                    