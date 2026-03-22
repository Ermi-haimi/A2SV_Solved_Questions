class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        mx=-float('inf')
        for num in nums:
            curr += num
            mx = max(curr,mx)
            if(curr <0):
                curr = 0
        
        return mx 

        