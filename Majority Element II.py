from collections import defaultdict
class Solution:
    def majorityElement(self, nums):
        n =len(nums)//3
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        ans = []
        for key, item in freq.items():
            if(item > n):
                ans.append(key)
        return ans