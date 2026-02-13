class Solution:
    def longestConsecutive(self, nums) -> int:
        n = len(nums)
        s = set(nums)
        nums = list(s)
        count = 0
        mx_count = 0
        for ind,num in enumerate(nums):
            count =1
            if num-1 in s:
                pass
            else:
                curr = nums[ind]
                while(curr+1 in s):
                    count+=1
                    curr +=1 
                mx_count = max(count, mx_count)
        
        return mx_count