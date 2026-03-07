class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        pre_seen = defaultdict(int)
        pre_seen[0]=1
        curr = 0
        count=0
        for i in range(n):
            curr+=nums[i]
            count+=pre_seen[curr-k]
            pre_seen[curr]+=1 
        return count