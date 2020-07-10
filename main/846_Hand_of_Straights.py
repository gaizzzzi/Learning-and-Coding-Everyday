class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W: 
            return False
        counter = collections.Counter(hand)
        hand.sort()
        for card in hand:
            if not counter[card]:
                continue
            for i in range(W):
                if counter[card + i]:
                    counter[card + i] -= 1
                else:
                    return False
        return True