class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        child_map = defaultdict(list)
        for i in range(len(pid)):
            child_map[ppid[i]].append(pid[i])
        ans = [kill]
        i = 0
        while i < len(ans):
            ans.extend(child_map[ans[i]])
            i += 1
        return ans