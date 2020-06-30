class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # 15:55 - 15:56 one pass
        balloon = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for char in text:
            if char in balloon:
                balloon[char] += 1
        balloon["l"] //= 2
        balloon["o"] //= 2
        return min(balloon.values())