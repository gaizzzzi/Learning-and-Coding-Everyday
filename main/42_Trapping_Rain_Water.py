class Solution:
    def trap(self, height: List[int]) -> int:
        # 18:30 - 19:29
        # decreasing stack
        if not height:
            return 0
        stack = []
        rain = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if stack:
                    rain += (min(height[i], height[stack[-1]]) - height[top]) * (i - stack[-1] - 1)
            stack.append(i)
        return rain