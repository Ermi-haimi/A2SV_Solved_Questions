class Solution:
    def isCovered(self, ranges, left: int, right: int) -> bool:
        lr = set(i for i in range(left, right+1))
        check = set()
        for nums in ranges:
            check.update(set(i for i in range(nums[0], nums[1]+1)))
        
        return lr<= check