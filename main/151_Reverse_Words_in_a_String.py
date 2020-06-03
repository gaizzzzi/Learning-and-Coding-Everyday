class Solution:
    def reverseWords(self, s: str) -> str:
        # 18:03-18:10
        new_s = ""
        tmp = ""
        for x in s[::-1]:
            if x == " ":
                if tmp:
                    new_s += " " + tmp[::-1]
                    tmp = ""
                continue
            else:
                tmp += x
        if tmp:
            new_s += " " + tmp[::-1]
        return new_s[1:]