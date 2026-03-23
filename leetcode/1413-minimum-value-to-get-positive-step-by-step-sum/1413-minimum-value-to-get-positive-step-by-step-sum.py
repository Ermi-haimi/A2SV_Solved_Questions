class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        
        mn = min(nums)
        ans = 1
        if(mn <0 ):
            ans = (-1*mn)+1
        return ans
            
