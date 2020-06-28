class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort(reverse = True)
        n = len(arr)
        while n and arr[n - 1] * n < target:
            n -= 1
            target -= arr[n]
        return round((target - 0.0001) / n) if n else arr[0]