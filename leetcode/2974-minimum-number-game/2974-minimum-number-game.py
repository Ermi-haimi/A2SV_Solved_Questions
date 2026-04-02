class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        nums.sort()
        n = len(nums)
        for i in range(0,n-1,2):
            arr.append(nums[i+1])
            arr.append(nums[i])
        return arr