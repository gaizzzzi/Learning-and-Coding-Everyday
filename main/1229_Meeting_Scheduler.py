class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # 17:48 - 17:50 one pass 
        slots = sorted(slots1 + slots2)
        pre_start, pre_end = slots[0]
        for start, end in slots[1:]:
            if pre_start <= start < pre_end:
                if duration <= min(pre_end, end) - start:
                    return [start, start + duration]
            pre_start, pre_end = start, end
        return []
        