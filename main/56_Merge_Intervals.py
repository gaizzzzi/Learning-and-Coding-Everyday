class Solution:
    def merge_heap_100ms(self, intervals: List[List[int]]) -> List[List[int]]:
        # NlogN
        hp = []
        for interval in intervals:
            heappush(hp, (interval[0], False))
            heappush(hp, (interval[1], True))
        end_flag = True
        first_start = last_end = 0
        ans = []
        start_count = 0
        while hp:
            point, if_end = heappop(hp)
            if not if_end and end_flag and start_count == 0:
                ans.append([first_start, last_end])
                first_start = point
            if not if_end:
                start_count += 1
                end_flag = False
            if if_end:
                last_end = point
                end_flag = True
                start_count -= 1

    def merge_stack_92ms(self, intervals: List[List[int]]) -> List[List[int]]:
        # NlogN
        points = []
        for interval in intervals:
            points.append((interval[0], "0"))
            points.append((interval[1], "1")) 
            # make sure if start and end got the same value, start is always in the front of end  
        points.sort()
        stack = []
        ans = []
        for point in points:
            if point[1] == "1":
                start = stack.pop()
                if not stack:
                    ans.append([start, point[0]])
            else:
                stack.append(point[0])
        return ans

    def merge_normal_88ms(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        ans = []
        start = intervals[0][0]
        end = intervals[0][1]
        for c_start, c_end in intervals[1:]:
            if c_start > end:
                ans.append([start, end])
                start = c_start
                end = c_end
            if c_end > end:
                end = c_end
        ans.append([start, end])
        return ans
