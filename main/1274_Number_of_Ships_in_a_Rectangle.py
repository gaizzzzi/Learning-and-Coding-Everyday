# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        #print(topRight.x, topRight.y, bottomLeft.x, bottomLeft.y)
        if (topRight.x == bottomLeft.x) and (topRight.y == bottomLeft.y) and sea.hasShips(topRight, bottomLeft):
            return 1
        mid = Point((bottomLeft.x + topRight.x + 1) // 2, (bottomLeft.y + topRight.y + 1) // 2)
        count = 0
        if (topRight.y >= mid.y and topRight.x >= mid.x) and \
            sea.hasShips(topRight, mid):
            count += self.countShips(sea, topRight, mid)
        if mid.x - 1 >= bottomLeft.x and mid.y - 1 >= bottomLeft.y and \
            sea.hasShips(Point(mid.x - 1, mid.y - 1), bottomLeft):
            count += self.countShips(sea, Point(mid.x - 1, mid.y - 1), bottomLeft)
        if mid.x - 1 >= bottomLeft.x and topRight.y >= mid.y and \
            sea.hasShips(Point(mid.x - 1, topRight.y), Point(bottomLeft.x, mid.y)):
            count += self.countShips(sea, Point(mid.x - 1, topRight.y), Point(bottomLeft.x, mid.y))
        if topRight.x >= mid.x and mid.y - 1 >= bottomLeft.y and \
            sea.hasShips(Point(topRight.x, mid.y - 1), Point(mid.x, bottomLeft.y)):
            count += self.countShips(sea, Point(topRight.x, mid.y - 1), Point(mid.x, bottomLeft.y))
        return count
            