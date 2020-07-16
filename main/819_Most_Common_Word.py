class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counter = defaultdict(int)
        tmp, maxcount, maxword = "", 0, ""
        for char in paragraph:
            if char.isalpha():
                tmp += char.lower()
            else:
                if tmp and not tmp in banned:
                    counter[tmp] += 1
                    if maxcount < counter[tmp]:
                        maxcount, maxword = counter[tmp], tmp
                        
                tmp = ""
        if tmp and not tmp in banned:
            counter[tmp] += 1
            if maxcount < counter[tmp]:
                maxcount, maxword = counter[tmp], tmp
        return maxword