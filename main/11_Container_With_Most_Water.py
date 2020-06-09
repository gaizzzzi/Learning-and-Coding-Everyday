class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 17:20
        left, right = 0, len(height) - 1
        maxarea = 0
        while left < right:
            maxarea = max(min(height[left], height[right]) * (right - left), maxarea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxarea
                
                