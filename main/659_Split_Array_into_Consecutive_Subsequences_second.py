class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        close = {}
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        k = 3
        for num in nums:
            if not count[num]:
                continue
            count[num] -= 1
            if close.get(num - 1) is not None and close.get(num - 1) > 0:
                close[num - 1] -= 1
                close[num] = close.get(num, 0) + 1
            else:
                for i in range(1, k):
                    if count.get(num + i) is not None and count.get(num + i) > 0:
                        count[num + i] -= 1
                    else:
                        return False
                close[num + k - 1] = close.get(num + k - 1, 0) + 1
        return True
        