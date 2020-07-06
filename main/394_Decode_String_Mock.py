class Solution:
    def decoding_string(self, s):
        def helper(pos):
            tmp_s = ""
            while pos < len(s) and s[pos] != "]":
                if s[pos].isdigit():
                    decoded_s, decoded_pos = helper(pos + 2)
                    tmp_s += decoded_s * int(s[pos])
                    pos = decoded_pos
                else:
                    tmp_s += s[pos]
                pos += 1

            return tmp_s, pos
        decoded_s, pos = helper(0)
        return decoded_s

# pos = 0:
#     tmp_s = "accaccacc", 8
#     pos = 8:
#         tmp_s = "accaccacc" 
#     pos = 7:
#         tmp_s = "a" + "cc"
#         pos = 5:
#             tmp_s = "c"
#         pos = 6:
