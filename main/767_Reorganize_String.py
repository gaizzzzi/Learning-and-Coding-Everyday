class Solution:
    def reorganizeString(self, S: str) -> str:
        # one pass
        count = collections.Counter(S)
        if count.most_common(1)[0][1] > (len(S) + 1) // 2:
            return ""
        
        first_char, l = count.most_common(1)[0]
        count[first_char] = 0
        ans = first_char * l
        loop, idx = 2, 0
        while count.most_common(1)[0][1]:
            first_char, tmp = count.most_common(1)[0]
            count[first_char] = 0
            while tmp:
                ans = ans[:loop * idx + 1] + first_char + ans[loop * idx + 1:]
                idx = (idx + 1) % l
                if not idx:
                    loop += 1
                count[first_char] -= 1
                tmp -= 1
        return ans