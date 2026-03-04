from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        freq = Counter(nums)
        for key,val in freq.items():
            if(val >n//3):
                ans.append(key)
        
        return ans