class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # 19:30 - 20:06
        interval = [0] * n
        stack = []
        log_list = []
        for log in logs:
            function, is_end, time = log.split(":")
            log_list.append((int(time), int(is_end == "end") , int(function)))
        log_list.sort()
        

        for log in log_list:
            if not stack or not log[1]:
                stack.append((log[0], log[-1]))
            elif log[-1] == stack[-1][-1]:
                tmp = stack.pop()
                t = log[0] - tmp[0] + 1
                interval[tmp[-1]] += t
                if stack:
                    interval[stack[-1][-1]] -= log[0] - tmp[0] + 1
          
        return interval