class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def permute(done,arr,step):
            if(step == n ):
                ans.append(done)
                return
            for i in range(step+1):
                newdone=done[:i]+[arr[step]]+done[i:]
                permute(newdone,arr,step+1)
        
        permute([],nums,0)
        return ans