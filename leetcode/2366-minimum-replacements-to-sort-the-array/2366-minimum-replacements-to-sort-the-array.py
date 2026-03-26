from math import floor,ceil
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        i = n-2
        def counter(arr,num2,p):
            nonlocal count
            if(p <0):
                return
            if(arr[p] > num2):
                k = ceil(arr[p]/num2)
                count+=k-1
                num2 = floor(arr[p]/k)
                counter(arr,num2,p-1)
            else:
                num2 = arr[p]
                print(arr[p],num2,count)
                counter(arr,num2,p-1)
        counter(nums,nums[-1],i)
        return count