class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        idx, count, prev = 1, 1, chars[0]
        while idx < len(chars):
            if chars[idx] == prev:
                count += 1
                chars.pop(idx)
            elif chars[idx] != prev:
                prev = chars[idx]
                if count > 1:
                    for bit in str(count)[::-1]:
                        chars.insert(idx, bit)
                    idx += 1
                idx = idx + len(str(count))
                count = 1
        if count > 1:
            chars += list(str(count))
        return len(chars)