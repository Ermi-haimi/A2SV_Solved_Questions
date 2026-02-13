from collections import Counter
class Solution:
    def minimumIndex(self, nums) -> int:
        n= len(nums)
        freq = Counter(nums)
        right = 0
        dominant = 0
        for key,val in freq.items():
            if(val>right):
                right = val
                dominant = key
        left = 0
        for ind,num in enumerate(nums):
            if(num == dominant):
                left +=1
                right-=1
                if(left>(ind+1)/2 and right>(n-(ind+1))/2):
                    return ind
        
        return -1

        