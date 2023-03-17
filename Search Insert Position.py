class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        for i in range(0, n):
            if(nums[i] == target):
                result = i
                break
            
        if(i == n - 1):
            nums.append(target)
            nums.sort()
            result = nums.index(target)
        
        return result
        
                
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """