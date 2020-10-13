class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_log, dig_log = [], []
        for log in logs:
            tmp = log.split(" ", maxsplit = 1)
            if tmp[1][0].isalpha():
                let_log.append([tmp[1], tmp[0]])
            else:
                dig_log.append(log)
        return [y + " " + x for x, y in sorted(let_log)] + dig_log
       
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def comparison_rule(log):
            tmp = log.split(" ", maxsplit = 1)
            if tmp[1][0].isalpha():
                return (0, tmp[1], tmp[0])
            else:
                return (1, '', '')
        return sorted(logs, key = comparison_rule)