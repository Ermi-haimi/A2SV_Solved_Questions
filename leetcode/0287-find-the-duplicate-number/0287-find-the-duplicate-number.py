class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i =0
        n = len(nums)
        while(i<n):
            if(nums[i] != i+1 and nums[i] != nums[nums[i]-1]):
                temp= nums[i]
                nums[i]=nums[temp-1]
                nums[temp-1] = temp
            else:
                i+=1
        print(nums)
        for ind,num in enumerate(nums):
            if(num != ind+1):
                return num
        return -1
            