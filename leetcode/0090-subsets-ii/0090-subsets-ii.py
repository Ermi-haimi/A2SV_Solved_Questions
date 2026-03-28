class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        seen = set()
        def sub2(arr,i):
            if(i==n):
                if(tuple(arr) not in seen):
                    ans.append(arr[:])
                    seen.add(tuple(arr[:]))
                return
            arr.append(nums[i])
            sub2(arr,i+1)
            arr.pop()
            sub2(arr,i+1)
        sub2([],0)
        return ans