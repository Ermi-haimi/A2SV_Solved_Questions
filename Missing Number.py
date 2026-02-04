class Solution:
    def missingNumber(self, nums) -> int:
        i = 0
        n = len(nums)
        while(i<len(nums)):
            if(i == nums[i] or nums[i]>=n):
                i+=1
            else:
                temp = nums[nums[i]] 
                nums[nums[i]] = nums[i]
                nums[i] = temp 
            
        for i in range(n):
            if(nums[i] != i):
                return i
        
        return n
