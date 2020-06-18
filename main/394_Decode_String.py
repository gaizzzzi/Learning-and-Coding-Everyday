class Solution:
    def decodeString(self, s: str) -> str:
        tmp = None
        s_list = []
        for char in s:
            if char.isdigit():
                tmp = int(char) if tmp is None else tmp * 10 + int(char)
            else: 
                if not tmp is None:
                    s_list.append(tmp)
                    tmp = None
                s_list.append(char)
                
        def helper(pos):
            tmp = ""
            while pos < len(s_list) and s_list[pos] != "]":
                if isinstance(s_list[pos], int):
                    _tmp, _pos = helper(pos + 2)
                    tmp += _tmp * s_list[pos]
                    pos = _pos
                else:
                    tmp += s_list[pos]
                    pos += 1
            return tmp, pos + 1
        
        pos = 0
        return helper(0)[0]