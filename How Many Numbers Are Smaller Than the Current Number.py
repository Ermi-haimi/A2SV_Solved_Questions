class Solution:
    def smallerNumbersThanCurrent(self, nums):
        nums_copy = nums[:]
        nums.sort()
        smallers = {}
        for ind,num in enumerate(nums):
            if num not in smallers:
                smallers[num] = ind
        
        for ind,num in enumerate(nums_copy):
            nums_copy[ind] = smallers[num]
        
        return nums_copy
            