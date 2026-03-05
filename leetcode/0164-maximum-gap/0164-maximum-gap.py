class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        nums.sort()
        mx = 0
        for i in range(n-1):
            mx = max(mx,abs(nums[i]-nums[i+1]))
        return mx
