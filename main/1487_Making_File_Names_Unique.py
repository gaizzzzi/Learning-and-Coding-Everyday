class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        n_map = {}
        ans = []
        for name in names:
            tmp = 0
            if name in n_map:
                tmp = n_map[name]
                while name + "(" + str(tmp) + ")" in n_map:
                    tmp += 1
            
            n_map[name] = tmp + 1
            if tmp:
                ans.append(name + "(" + str(tmp) + ")")
                n_map[name + "(" + str(tmp) + ")"] = 1
            else:
                ans.append(name)
        return ans