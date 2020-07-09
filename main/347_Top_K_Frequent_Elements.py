class Solution:
    def topKFrequent_hp(self, nums: List[int], k: int) -> List[int]:
        int_counter = collections.Counter(nums)
        hp = []
        for integer, count in int_counter.items():
            if len(hp) < k:
                heappush(hp, (count, integer))
            else:
                if hp[0][0] < count:
                    heappushpop(hp, (count, integer))
        return [y for x, y in hp]

    def topKFrequent_partition(self, nums: List[int], k: int) -> List[int]:
        counter = list(collections.Counter(nums).items())
        def partition(lo, hi, counter, k):
            l, r, random_idx = lo, hi, int(random.random() * (hi - lo) + lo)
            counter[random_idx], counter[lo] = counter[lo], counter[random_idx]
            pivot = counter[lo]
            while l < r:
                while l < hi and counter[l][1] >= pivot[1]:
                    l += 1
                while r > lo and counter[r][1] <= pivot[1]:
                    r -= 1
                if l < r:
                    counter[l], counter[r] = counter[r], counter[l]
            counter[lo], counter[r] = counter[r], counter[lo]
            if r == k - 1:
                return
            elif r < k - 1:
                partition(r + 1, hi, counter, k)
            else:
                partition(lo, r - 1, counter, k)
        partition(0, len(counter) - 1, counter, k)
        return [x for x, y in counter[:k]]

    def topKFrequent_bucket_sort(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        bucket = [[] for _ in range(max(counter.values()))]
        for integer, count in counter.items():
            bucket[count - 1].append(integer)
        ans = []
        for x in bucket[::-1]:
            ans.extend(x)
            if len(ans) == k:
                return ans
        