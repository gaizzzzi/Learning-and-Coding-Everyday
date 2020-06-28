# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        # find peak
        l, r = 0, n - 1
        while l < r - 1:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid
            else:
                r = mid
        if mountain_arr.get(l) < mountain_arr.get(r):
            peak = r
        else:
            peak = l
        
        if mountain_arr.get(peak) == target:
            return peak
        
        # find before peak
        l, r = 0, peak - 1
        while l < r - 1:
            mid = (l + r) // 2
            mid_v = mountain_arr.get(mid)
            if mid_v == target:
                return mid
            elif mid_v < target:
                l = mid
            else:
                r = mid
        if mountain_arr.get(l) == target:
            return l
        if mountain_arr.get(r) == target:
            return r
        
        # find after peak
        l, r = peak + 1, n - 1
        while l < r - 1:
            mid = (l + r) // 2
            mid_v = mountain_arr.get(mid)
            if mid_v == target:
                return mid
            elif mid_v < target:
                r = mid
            else:
                l = mid
        if mountain_arr.get(l) == target:
            return l
        if mountain_arr.get(r) == target:
            return r
        
        return -1
        