class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans, stack = [0] * len(T), []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                tmp = stack.pop()
                ans[tmp] = i - tmp 
            stack.append(i)
        return ans