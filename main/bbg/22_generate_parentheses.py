def generate_parentheses(n):

    def helper(left, right):
        if not left and not right:
            return [""]
        tmp = []
        for bracket in "()":
            if left and bracket == "(":
                tmp.extend([bracket + t for t in helper(left - 1, right)])
            if right > left and bracket == ")":
                tmp.extend([bracket + t for t in helper(left, right - 1)])
        return tmp
    return helper(n, n)
