class Solution:
    def twoSum(self, nums, target):
        indices={}
        for ind,num in enumerate(nums):
            indices[num] = ind
        ans = []
        for ind,num in enumerate(nums):
            if target-num in indices:
                if(indices[target-num]!= ind):
                    ans.append(ind)
                    ans.append(indices[target-num])
                    break
        
        return ans