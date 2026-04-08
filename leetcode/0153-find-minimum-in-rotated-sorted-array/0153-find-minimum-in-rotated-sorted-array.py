class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        mount = -1

        while(left <= right):
            mid = left + (right-left)//2
            if(mid+1<n and nums[mid] > nums[mid+1]):
                mount = mid
                break
            elif(nums[mid] >= nums[-1] and nums[mid] >= nums[0]):
                left = mid+1
            else:
                right = mid-1
        if(mount == n-1):
            return nums[0]
        return nums[mount+1]
            
        