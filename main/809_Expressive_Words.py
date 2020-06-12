class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        # 17:23 - 17:40
        if not S:
            return len([1 for word in words if word == ""])
        
        char_list = [[S[0], 1]]
        for i in range(1, len(S)):
            if S[i] != S[i - 1]:
                char_list.append([S[i], 1])
            else:
                char_list[-1][1] += 1
        
        ans = 0
        for word in words:
            start = 0
            i = 0
            while i < len(word):
                if word[i] == char_list[start][0]:
                    i += 1
                    count = 1
                    while i < len(word) and word[i] == word[i - 1]:
                        i += 1
                        count += 1
                    if count < char_list[start][1] < 3 \
                        or count > char_list[start][1]:
                        break
                    start += 1
                else:
                    break
            if i == len(word) and start == len(char_list):    
                ans += 1
        return ans
        