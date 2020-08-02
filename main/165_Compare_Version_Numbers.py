class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # beat 82.84%
        vlist1 = version1.split(".")
        vlist2 = version2.split(".")
        i = 0
        while i < max(len(vlist1), len(vlist2)):
            vlevel1 = int(vlist1[i]) if i < len(vlist1) else 0
            vlevel2 = int(vlist2[i]) if i < len(vlist2) else 0
            if vlevel1 < vlevel2:
                return -1
            elif vlevel1 > vlevel2:
                return 1
            i += 1
        
        return 0