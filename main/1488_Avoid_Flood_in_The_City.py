class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        lakes = {}
        empty = []
        for i, lake in enumerate(rains):
            if lake > 0:
                ans[i] = -1
                if lake in lakes:
                    if not empty or empty[-1] < lakes[lake]:
                        return []
                    else:
                        j = 0
                        while empty[j] < lakes[lake]:
                            j += 1
                        tmp = empty.pop(j)
                        ans[tmp] = lake
                        
                lakes[lake] = i
                        
            else:
                empty.append(i)
        return ans