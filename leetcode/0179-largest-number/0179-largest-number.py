class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for ind,num in enumerate(nums):
            nums[ind] = str(num) 
        
        def custom_sort(num1, num2):
            if(num1+num2 > num2+num1):
                return -1
            else:
                return 1
        
        nums = sorted(nums, key=cmp_to_key(custom_sort))
        if nums[0] == "0":
            return "0"
        return "".join(nums)