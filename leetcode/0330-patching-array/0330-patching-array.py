class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i =0
        count = 0
        mx = 1
        while(mx<=n):
            if(i<len(nums) and nums[i]<=mx):
                mx+=nums[i]
                i+=1
            else:
                count +=1
                mx = mx*2
        return count
