class Solution:
    def countPairs(self, nums, k: int) -> int:
        ans = 0
        indices = {}
        for ind,num in enumerate(nums):
            if(num in indices):
                for i in indices[num]:
                    if (ind*i)%k==0:
                        ans+=1
                indices[num].append(ind)
            else:
                indices[num] = [ind]
        
        return ans
        