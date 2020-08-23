class Solution:
    def reverseBits(self, n: int) -> int:
        rev_n, i = 0, 31
        while n:
            rev_n |= (n & 1) << i
            n, i = n >> 1, i - 1
        return rev_n
    def reverseBits_mask_and_shift(self, n: int) -> int:
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n