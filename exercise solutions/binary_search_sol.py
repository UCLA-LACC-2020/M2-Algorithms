def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        mid = int((low + high)/2)
        
        if len(nums) == 0:
            return -1
        
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        
        while low + 1 < high:
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                low = mid+1
            elif target< nums[mid]:
                high = mid-1
            mid = int((low + high)/2)
            
        if nums[low] == target:
            return low
        
        if nums[high] == target:
            return high
        
        return -1