class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]*n
        prod = 1
        for i in range(n):
            left[i]=prod
            prod *= nums[i]
            
        right = [1]*n
        prod = 1
        for i in range(n-1,-1,-1):
            right[i]=prod
            prod *= nums[i]
        
        
        ans =[left[i]*right[i] for i in range(n)]
        
            
        
        return ans
        