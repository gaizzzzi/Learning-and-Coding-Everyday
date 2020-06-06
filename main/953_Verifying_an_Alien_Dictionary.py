class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 19:20 - 19:29
        if len(words) < 2:
            return True
        letter_map = {}
        for i in range(len(order)):
            letter_map[order[i]] = i
        for i in range(1, len(words)):
            for j in range(0, len(words[i - 1])):
                if j == len(words[i]):
                    return False
                if letter_map[words[i - 1][j]] > letter_map[words[i][j]]:
                    return False
                if letter_map[words[i - 1][j]] < letter_map[words[i][j]]:
                    break
        return True