class Solution(object):

'''
for students: if you are using it as a standalone function, please use
def sortArray(nums):
i.e. remove the "self"
'''
############ bubble sort
    #     def sortArray(self, nums):
    #         """
    #         :type nums: List[int]
    #         :rtype: List[int]
    #         """
    #         if len(nums) <= 1:
    #             return nums

    #         for j in range(0, len(nums) - 1):
    #             for i in range(0, len(nums) - j -1):
    #                 if nums[i] > nums[i+1]:
    #                     temp = nums[i+1]
    #                     nums[i+1] = nums[i]
    #                     nums[i] = temp
    #         return nums


############ python build-in sort
    # def sortArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     nums.sort()
    #     return nums

    
############ insert sort
#     def sortArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         if len(nums) <= 1:
#             return nums

#         for i in range(1, len(nums)):

#             for j in range(0, i):
#                 if nums[j] > nums[i]:
#                     temp = nums[i]
#                     for k in range(i, j, -1):
#                         nums[k] = nums[k - 1]
#                     nums[j] = temp
#         return nums    
    
############ quick sort
#     def shuffle(self, nums):
#         pass

#     def partition(self, nums):
#         k = 0
#         i = 1
#         j = len(nums) - 1
#         while True:
#             while  j >= 0 and nums[j] > nums[k]:
#                 j -= 1
#             while i <= len(nums) - 1 and nums[i] < nums[k]:
#                 i += 1
#             if i >= j:
#                 break
#             temp = nums[i]
#             nums[i] = nums[j]
#             nums[j] = temp
#         temp = nums[k]
#         nums[k] = nums[j]
#         nums[j] = temp
#         return nums, j


#     def sortArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         if len(nums) <= 1:
#             return nums
#         nums, j = self.partition(nums)
#         left_part = self.sortArray(nums[0:j])
#         center_part = nums[j]
#         right_part = self.sortArray(nums[j+1:len(nums)+1])
#         nums = []
#         nums.extend(left_part)
#         nums.append(center_part)
#         nums.extend(right_part)
#         return nums


############ Merge Sort
    def merge(self, a, b):
        result = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        if i < len(a):
            while i < len(a):
                result.append(a[i])
                i += 1
        if j < len(b):
            while j < len(b):
                result.append(b[j])
                j += 1
        return result
    
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        mid = int(round(len(nums)/2))
        left_part = self.sortArray(nums[0:mid])
        right_part = self.sortArray(nums[mid: len(nums)+1])
        return self.merge(left_part, right_part)
        
    