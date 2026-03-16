from collections import Counter
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre_seen = defaultdict(int)
        pre_seen[0] =1 
        ans = 0
        curr = 0
        for num in nums:
            curr+=num
            ans+=pre_seen[curr%k]
            pre_seen[curr%k]+=1
        return ans

        