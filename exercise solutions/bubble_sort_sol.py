#Functions for sorting exercise

def cmp(a, b):
    return (a > b) - (a < b) 

def mySort(numbers):
    numbers = bubbleSort(numbers)
    return numbers

def bubbleSort(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if len(nums) <= 1:
        return nums

    for j in range(0, len(nums) - 1):
        for i in range(0, len(nums) - j -1):
            if nums[i] > nums[i+1]:
                temp = nums[i+1]
                nums[i+1] = nums[i]
                nums[i] = temp
    return nums