
class Solution:
    def depthSum(self, nestedList: List[NestedInteger], depth = 1) -> int:
        tmp_sum = 0
        for element in nestedList:
            if element.isInteger():
                tmp_sum += depth * element.getInteger()
            else:
                tmp_sum += self.depthSum(element.getList(), depth + 1)
        return tmp_sum