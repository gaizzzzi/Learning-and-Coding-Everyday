class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        def topk(k, num1, num2):
            if len(num1) > len(num2):
                num1, num2 = num2, num1
            
            if not num1: 
                return num2[k - 1]
            
            if k == 1:
                return num1[0] if num1[0] < num2[0] else num2[0]
            
            halfk = min(k // 2, len(num1))
            if num1[halfk - 1] > num2[halfk - 1]:
                return topk(k - halfk, num2[halfk:], num1)
            else:
                return topk(k - halfk, num1[halfk:], num2)
        
        k = (len(num1) + len(num2) + 1) // 2
        if (len(num1) + len(num2)) % 2:
            return topk(k, num1, num2) / 1.0
        else:
            return (topk(k, num1, num2) + topk(k + 1, num1, num2)) / 2