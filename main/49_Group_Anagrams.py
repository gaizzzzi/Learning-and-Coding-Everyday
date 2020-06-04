class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 22:40 - 22:45
        str_map = {}
        for s in strs:
            ssort = "".join(sorted(s))
            if str_map.get(ssort) is None:
                str_map[ssort] = [s]
            else:
                str_map[ssort] += [s]
        return list(str_map.values())