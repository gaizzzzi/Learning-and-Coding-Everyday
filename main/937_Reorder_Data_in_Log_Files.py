class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_log, letter_log = [], []
        for log in logs:
            tmp = log.split(" ")
            if "a" <= tmp[1][0] <= "z":
                letter_log.append([" ".join(tmp[1:]), tmp[0]])
            else:
                digit_log.append(log)
                
        letter_log.sort()
        return [" ".join(x[::-1]) for x in letter_log] + digit_log