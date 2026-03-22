class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n= len(nums)
        rem = {}
        rem[0]=-1
        curr = 0
        for i in range(n):
            curr+=nums[i]
            r = curr%k
            if(r not in rem):
                rem[r]=i
            else:
                if(i-rem[r] >=2):
                    return True
            
        return False

        