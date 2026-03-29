class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        n = len(nums)
        for i in range(n):
            if(nums[i]==0):
                if(i+2<=n-1):
                    count+=1
                    nums[i],nums[i+1],nums[i+2] =1,abs(nums[i+1]-1),abs(nums[i+2]-1)
        
        if(sum(nums) ==n):
            return count
        return -1