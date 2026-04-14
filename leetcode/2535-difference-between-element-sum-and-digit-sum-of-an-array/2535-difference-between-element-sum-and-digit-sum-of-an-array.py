class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        tot = sum(nums)
        s = 0
        for num in nums:
            while(num >0):
                s+=num%10
                num = num//10
        return abs(tot-s)