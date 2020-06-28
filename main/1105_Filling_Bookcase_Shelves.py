class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        dp = [0] + [float('inf')] * len(books)
        
        # dp[i] means min height of i - 1 books
        for i in range(len(books) + 1):
            cur_width, cur_height = shelf_width, 0
            j = i - 1
            # update dp[i] min height for previous books that could be in one shelf one by one.
            while j >= 0 and cur_width - books[j][0] >= 0:
                cur_height = max(cur_height, books[j][1])
                cur_width -= books[j][0]
                dp[i] = min(dp[i], dp[j] + cur_height)
                j -= 1
        
        return dp[-1]