class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        req = [0]*(n+1)
        for left,right in requests:
            req[left]+=1
            req[right+1] -=1

        for i in range(1,n):
            req[i] += req[i-1]
        req_ind = {}
        for ind,r in enumerate(req):
            req_ind[ind] = r
        
        req_ind = dict(sorted(req_ind.items(),reverse=True , key=lambda x:x[1]))
        c_nums = [0]*(n+1)
        nums = sorted(nums, reverse=True)
        ni = 0
        
        nums.append(0)

        for key,val in req_ind.items():
            c_nums[key] = nums[ni]
            ni+=1

        for i in range(1,n):
            c_nums[i] += c_nums[i-1]
        
        ans = 0
        for left,right in requests:
            if(left >0):
                curr = c_nums[right]-c_nums[left-1]
            else:
                curr = c_nums[right]
            ans += curr
        return ans%((10**9)+7)
        

        
        


        