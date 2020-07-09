class Solution:
    def leastInterval_math(self, tasks: List[str], n: int) -> int:
        task_counter = list(collections.Counter(tasks).values())
        top_n = max(task_counter)
        num_top_n = task_counter.count(top_n)
        return max((n + 1) * (top_n - 1) + num_top_n, len(tasks))

    def leastInterval_hp(self, tasks: List[str], n: int) -> int:
        task_counter, hp = collections.Counter(tasks), []
        for task, count in task_counter.items():
            heappush(hp, (-count, task))
        
        time_used = 0
        while hp:
            k, tmp = 0, []
            while k < n + 1 and hp:
                tmp.append(heappop(hp))
                k += 1
            while tmp:
                count, task = tmp.pop()
                if count + 1:
                    heappush(hp, (count + 1, task))
            if hp:
                time_used += n + 1
            else:
                time_used += k
        return time_used
                
            