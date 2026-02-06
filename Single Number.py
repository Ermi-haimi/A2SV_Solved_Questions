class Solution:
    def singleNumber(self, nums) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        
        for num in seen:
            return num