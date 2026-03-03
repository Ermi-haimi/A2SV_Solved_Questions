class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        mx = 0
        d = 0
        for right in range(len(nums)):
            if(nums[right] == 0):
                d+=1
            if(d>1):
                while(d > 1):
                    if(nums[left]==0):
                        d-=1
                    left+=1
            mx= max(mx, right-left+1)

        return mx-1
