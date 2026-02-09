class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        curr_even = 0
        for num in nums:
            if num%2 == 0:
                curr_even +=num
        
        ans = []

        for val,ind in queries:
            if((nums[ind] +val)%2 == 0):
                if nums[ind]%2==0:
                    curr_even -=nums[ind]
                    nums[ind] +=val
                    curr_even +=nums[ind]
                else:
                    nums[ind] +=val
                    curr_even +=nums[ind]
            else:
                if nums[ind]%2==0:
                    curr_even -=nums[ind]
                nums[ind] +=val
            ans.append(curr_even)
        
        return ans