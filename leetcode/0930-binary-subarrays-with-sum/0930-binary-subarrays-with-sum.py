from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre_seen = defaultdict(int)
        pre_seen[0] +=1
        curr = 0
        n = len(nums)
        count = 0
        for i in range(n):
            curr+=nums[i]
            count+=pre_seen[curr-goal]
            pre_seen[curr]+=1

        return count    