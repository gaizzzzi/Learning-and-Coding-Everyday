class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        string_group = defaultdict(list)
        for string in strings:
            first_char, key = ord(string[0]) , []
            for char in string:
                tmp = ord(char) - first_char
                key.append(str(tmp) if tmp > 0 else str(tmp + 26))
            string_group[".".join(key)].append(string)
        return [x for x in string_group.values()]