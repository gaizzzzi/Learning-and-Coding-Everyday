class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        def helper(s, record, last_op, last_val1, last_val2):
            if not s:
                if last_op == "+":
                    if last_val1 + last_val2 == target:
                        ans.append(record[1:])
                elif last_op == "*":
                    if last_val1 * last_val2 == target:
                        ans.append(record[1:])
                elif not last_op:
                    if last_val1 == target:
                        ans.append(record[1:])
                return
            for i in range(1, len(s) + 1):
                if i > 1 and s[0] == "0":
                    return
                val = int(s[:i])
                
                for op in ["+", "-", "*"]:
                    if op == "+":
                        if last_op == "+":
                            helper(s[i:], record + "+" + str(val), "+", last_val1 + last_val2, val)
                        elif last_op == "*":
                            helper(s[i:], record + "+" + str(val), "+", last_val1 * last_val2, val)
                    if s == num:
                        break
                    if op == "-":
                        if last_op == "+":
                            helper(s[i:], record + "-" + str(val), "+", last_val1 + last_val2, -val)
                        elif last_op == "*":
                            helper(s[i:], record + "-" + str(val), "+", last_val1 * last_val2, -val)
                        
                    if op == "*":
                        if last_op == "+":
                            helper(s[i:], record + "*" + str(val), "+", last_val1, last_val2 * val)
                        elif last_op == "*":
                            helper(s[i:], record + "*" + str(val), "*", last_val1 * last_val2, val)
            
        helper(num, "", "+", 0, 0)
        return ans