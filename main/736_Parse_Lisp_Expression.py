class Solution:
    def evaluate(self, expression: str) -> int:
        # 21:30 - 22:56
        def get_value(num_map, i):
            if expr[i] == "(":
                return helper(num_map, i + 1)
            elif expr[i] in num_map:
                return (num_map[expr[i]], i)
            else:
                return (int(expr[i]), i)
        
        def helper(num_map, pos):
            i = pos
            if expr[pos] == "add" or expr[pos] == "mult":
                # get num1 and num2
                num1, i = get_value(num_map, i + 1)
                num2, i = get_value(num_map, i + 1)
                
                return (num1 + num2, i + 1) if expr[pos] == "add" else (num1 * num2, i + 1)
            
            if expr[pos] == "let":
                # deep copy of num_map
                tmp_map = copy.deepcopy(num_map)
                    
                # deal with paras in let
                i += 1
                while i < len(expr):
                    if expr[i + 1] != ")" and expr[i] !="(":
                        num, j = get_value(tmp_map, i + 1)
                        tmp_map[expr[i]] = num
                        i = j + 1
                    else:
                        num, j = get_value(tmp_map, i)
                        return (num, j + 1)
                    
        # parse expression
        expr = ["("]
        tmp = ""
        for e in expression[1:]:
            if e == "(" or e == ")" or e == " ":
                if tmp:
                    expr.append(tmp)
                tmp = ""
                if e != " ":
                    expr.append(e)
            else:
                tmp += e
            
                    
        return helper({}, 1)[0]
            