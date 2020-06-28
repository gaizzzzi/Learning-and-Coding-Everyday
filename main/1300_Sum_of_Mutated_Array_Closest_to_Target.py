class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort(reverse = True)
        n = len(arr)
        while n and arr[n - 1] * n < target:
            n -= 1
            target -= arr[n]
        return round((target - 0.0001) / n) if n else arr[0]

    def findBestValue(self, arr: List[int], target: int) -> int:
        def get_sum(mid):
            tmp_sum = 0
            for num in arr:
                tmp_sum += min(num - mid, 0) + mid
            return tmp_sum
        
        l, r = 0, max(arr)
        
        while l < r - 1:
            mid = (l + r) // 2
            tmp_sum = get_sum(mid)
            if tmp_sum == target:
                return mid
            elif tmp_sum < target:
                l = mid
            else:
                r = mid
                
        l_v = abs(get_sum(l) - target) 
        r_v = abs(get_sum(r) - target)
        if l_v > r_v:
            return r
        else:
            return l