class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if not k:
            return s
        char_counter = collections.Counter(s)
        hp = []
        for char, count in char_counter.items():
            heappush(hp, (-count, char))
        
        ans = []
        while hp:
            n, tmp = 0, []
            while n < k and hp:
                tmp.append(heappop(hp))
                ans.append(tmp[-1][1])
                n += 1
            while tmp:
                count, char = tmp.pop()
                
                if count + 1:
                    heappush(hp, (count + 1, char))
            if n < k and hp:
                return ""
        return "".join(ans)