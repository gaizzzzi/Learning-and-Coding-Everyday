class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 16:49 - 16:58
        stack = []
        push_idx = 0
        pop_idx = 0
        while pop_idx < len(popped):
            while (not stack or stack[-1] != popped[pop_idx]) and push_idx < len(pushed):
                stack.append(pushed[push_idx])
                push_idx += 1
            
            if not stack or stack[-1] != popped[pop_idx]:
                return False
            
            while stack and stack[-1] == popped[pop_idx] and pop_idx < len(popped):
                p = stack.pop()
                pop_idx += 1
            
        return True