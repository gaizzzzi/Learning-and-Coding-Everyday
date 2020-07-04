class Solution:
    def maxRepOpt1(self, text: str) -> int:
        if not text:
            return 0
        char_count = []
        tot_char_count = collections.Counter(text)
        pre_char, count = text[0], 1
        for char in text[1:]:
            if char == pre_char:
                count += 1
            else:
                char_count.append((pre_char, count))
                count = 1
            pre_char = char
        char_count.append((pre_char, count))
        maxlen = 1
        for i, (char, count) in enumerate(char_count):
            if 0 < i < len(char_count) - 1 and count == 1:
                before, after = char_count[i - 1], char_count[i + 1]
                if before[0] == after[0]:
                    tmp = int(tot_char_count[before[0]] > before[1] + after[1])
                    maxlen = max(maxlen, before[1] + after[1] + tmp)
            maxlen = max(maxlen, count + int(tot_char_count[char] > count))
        return maxlen
                