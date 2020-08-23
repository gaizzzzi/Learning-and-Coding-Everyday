# 1 build class derived from str with customed compare function
class number(str):
    def __lt__(x, y):
        return x + y > y + x
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        tmp_largest_num = ''.join(sorted(map(str, nums), key = number))
        return '0' if tmp_largest_num[0] == '0' else tmp_largest_num

# 2 without building extra class but to use built-in function cmp_to_key from functools 
# with costumed comparison method
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        tmp_largest_num = ''.join(sorted(map(str, nums), key = cmp_to_key(lambda x, y: -1 if x + y > y + x else 1)))
        return '0' if tmp_largest_num[0] == '0' else tmp_largest_num