class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 18:03 - 18:15 one pass
        ans = []
        cur_len, cur_count = 0, 0
        
        def helper(start, end, l):
            if end - start == 1:
                return words[start] + " " * (maxWidth - len(words[start]))
            
            tmp = ""
            spaces = (maxWidth - l) // (end - start - 1)
            left_extra_spaces = (maxWidth - l) % (end - start - 1)
            for i, word in enumerate(words[start: end]):
                tmp += word
                if i < end - start - 1:
                    tmp += " " * (spaces + int(i < left_extra_spaces))
            return tmp
        
        for i, word in enumerate(words):
            if cur_len + len(word) + cur_count > maxWidth:
                ans.append(helper(i - cur_count, i, cur_len))
                cur_len, cur_count = len(word), 1
            else:
                cur_len += len(word)
                cur_count += 1
        
        tmp = " ".join(words[len(words) - cur_count:])
        ans.append(tmp + " " * (maxWidth - len(tmp)))
        return ans
                
        