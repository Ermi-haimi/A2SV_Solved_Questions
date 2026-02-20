class Solution:
    def largestPerimeter(self, nums):
        nums = sorted(nums, reverse=True)
        left = 0
        right = 3
        max_p = 0
        while(right<=len(nums)):
            arr = nums[left:right]
            if(arr[0]+arr[1] > arr[2] and arr[0]+arr[2] >arr[1] and arr[1]+arr[2]>arr[0]):
               return arr[0]+arr[1] +arr[2] 
            right+=1
            left+=1
        return 0