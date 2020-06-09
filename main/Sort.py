class Sort():
    def merge_sort(self, nums):
        # 17:28 - 17:38
        if len(nums) == 1:
            return nums
        num1 = self.merge_sort(nums[: len(nums)// 2])
        num2 = self.merge_sort(nums[len(nums) // 2:])
        # len(num1) <= len(num2)
        output = []
        i, j =0, 0
        while i < len(num1) and j < len(num2):
            if num1[i] < num2[j]:
                output.append(num1[i])
                i += 1
            else:
                output.append(num2[j])
                j += 1

        if i == len(num1):
            return output + num2[j:]
        if j == len(num2):
            return output + num1[i:]

    def quick_sort(self, nums, l, r):
        start, end = l, r
        pivot = l
        while start < end:
            while end > l and nums[end] >= nums[pivot]:
                end -= 1
            while start < r and nums[start] <= nums[pivot]:
                start += 1
            
            if start < end:
                nums[start], nums[end] = nums[end], nums[start]

        nums[end], nums[pivot] = nums[pivot], nums[end]

        if end - 1 > l:
            self.quick_sort(nums, l, end - 1) 
        if r > end + 1:
            self.quick_sort(nums, end + 1, r)

    def insertion_sort(self, nums):
        for i in range(1, len(nums)):
            j = i
            while j > 0 and nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1

    def bubble_sort(self, nums):
        sort_flag = False
        while not sort_flag:
            sort = True
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
                    sort = False



nums = [2,8,1,5,2,3,7,4]
s = Sort()
print("merge sort", s.merge_sort(nums))

s.quick_sort(nums, 0, len(nums) - 1)
print("quick sort",nums)

nums = [2,8,1,5,2,3,7,4]
s.insertion_sort(nums)
print("insertion sort",nums)

nums = [2,8,1,5,2,3,7,4]
s.insertion_sort(nums)
print("bubble sort",nums)
