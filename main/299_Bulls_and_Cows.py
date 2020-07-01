class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 17:47 - 17:51
        secret_count, guess_count = collections.Counter(), collections.Counter()
        bull, cows = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                secret_count[secret[i]] += 1
                guess_count[guess[i]] += 1
        
        for char, count in secret_count.items():
            cows += min(guess_count[char], count)
            
        return str(bull) + "A" + str(cows) + "B"