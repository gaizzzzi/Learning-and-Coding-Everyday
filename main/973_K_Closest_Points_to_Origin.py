class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance = []
        for i, (x, y) in enumerate(points):
            distance.append((x * x + y * y, i))
        
        def partition(lo, hi, points, K):
            l, r, random_idx = lo, hi, int(random.random() * (hi - lo) + lo)
            points[lo], points[random_idx] = points[random_idx], points[lo]
            pivot = points[lo][0]
            while l < r:
                while (l < hi) and points[l][0] <= pivot:
                    l += 1
                while (r > lo) and points[r][0] >= pivot:
                    r -= 1
                if l < r:
                    points[l], points[r] = points[r], points[l]
            points[lo], points[r] = points[r], points[lo]
            
            if r == K - 1:
                return r
            elif r < K - 1:
                return partition(r + 1, hi, points, K)
            else:
                return partition(lo, r - 1, points, K)
            
        ans = partition(0, len(distance) - 1, distance, K)
        return [points[i] for d, i in distance[:ans + 1]]
        